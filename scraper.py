import asyncio
import os
import re
import sys
from urllib.parse import urljoin, urlparse
import mimetypes
import logging
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from playwright.__main__ import main as playwright_main

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
TIMEOUT = 60000  # 60 segundos
MAX_RETRIES = 3
RETRY_DELAY = 10  # segundos

# Diretórios
SAVE_DIR = 'copart_clone/templates'
STATIC_DIR = 'copart_clone/static'

def install_playwright_browsers():
    """Instala os browsers necessários para o Playwright"""
    logger.info("Instalando browsers do Playwright...")
    try:
        # Simula a chamada via linha de comando
        original_argv = sys.argv
        sys.argv = ['playwright', 'install']
        playwright_main()
        sys.argv = original_argv
        logger.info("Browsers instalados com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao instalar browsers: {str(e)}")
        raise

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

async def scrape_page():
    """Faz scraping da página principal"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(
                    headless=True,
                    timeout=TIMEOUT
                )
                
                context = await browser.new_context(
                    user_agent=USER_AGENT,
                    viewport=VIEWPORT,
                    locale='pt-BR',
                    timezone_id='America/Sao_Paulo'
                )
                
                page = await context.new_page()
                
                try:
                    logger.info(f"Tentativa {attempt} para {BASE_URL}")
                    await page.goto(BASE_URL, timeout=TIMEOUT, wait_until='domcontentloaded')
                    
                    # Baixar assets
                    assets = await page.query_selector_all("""
                        link[href], script[src], img[src], source[src], 
                        video[src], audio[src], embed[src], object[data], iframe[src]
                    """)
                    
                    downloaded_assets = {}
                    for asset in assets:
                        src = await asset.get_attribute('href') or await asset.get_attribute('src') or await asset.get_attribute('data')
                        if src:
                            original_url, filename = await download_asset(page, src, BASE_URL)
                            if original_url and filename:
                                downloaded_assets[original_url] = filename
                    
                    # Processar conteúdo
                    content = await page.content()
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Atualizar referências para os assets baixados
                    for tag in soup.find_all(['link', 'script', 'img', 'source', 'video', 'audio', 'embed', 'object', 'iframe']):
                        attr = 'href' if tag.name == 'link' else ('src' if tag.has_attr('src') else 'data')
                        if tag.has_attr(attr):
                            original_url = tag[attr]
                            if original_url in downloaded_assets:
                                tag[attr] = f"/static/{downloaded_assets[original_url]}"
                    
                    # Salvar o HTML
                    os.makedirs(SAVE_DIR, exist_ok=True)
                    with open(os.path.join(SAVE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    logger.info(f"Página salva em {os.path.join(SAVE_DIR, 'index.html')}")
                    return True
                    
                finally:
                    await page.close()
                    await context.close()
                    await browser.close()
                    
        except Exception as e:
            logger.error(f"Erro na tentativa {attempt}: {str(e)}")
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY * attempt)
            continue
            
    return False

async def main():
    """Função principal"""
    logger.info("Iniciando scraping...")
    success = await scrape_page()
    if success:
        logger.info("Scraping concluído com sucesso!")
    else:
        logger.error("Falha ao raspar a página após várias tentativas")
    return success

if __name__ == "__main__":
    if '--install-only' in sys.argv:
        install_playwright_browsers()
        sys.exit(0)
        
    result = asyncio.run(main())
    sys.exit(0 if result else 1)

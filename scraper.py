import asyncio
from playwright.async_api import async_playwright
import os
import re
from urllib.parse import urljoin, urlparse
import mimetypes
import logging
from bs4 import BeautifulSoup

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configurações
BASE_URL = 'https://www.copart.com.br'  # Site original
TARGET_DOMAIN = 'www.copartbr.com.br'  # Seu domínio
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
VIEWPORT = {'width': 1280, 'height': 1024}
TIMEOUT = 120000

# Substituições
SUBSTITUTIONS = [
    (r'\(\d{2}\)\s\d{4,5}-\d{4}', '(11) 11 91471-9390'),
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'contato@copartbr.com.br'),
    (r'https?://www\.copart\.com\.br', f'https://{TARGET_DOMAIN}'),
    (r'//www\.copart\.com\.br', f'//{TARGET_DOMAIN}')
]

# Diretórios
SAVE_DIR = 'copart_clone/static'
STATIC_DIR = 'copart_clone/static'

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and result.scheme in ['http', 'https']
    except ValueError:
        return False

async def download_asset(page, url, base_url):
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
        
        # Processar arquivos CSS/JS
        if filename.endswith(('.css', '.js')):
            with open(filepath, 'r+', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for pattern, replacement in SUBSTITUTIONS:
                    content = re.sub(pattern, replacement, content)
                f.seek(0)
                f.write(content)
                f.truncate()
            
        return url, filename
        
    except Exception as e:
        logger.warning(f"Erro ao baixar {url}: {str(e)}")
        return None, None

async def crawl_site():
    visited = set()
    to_visit = [BASE_URL]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            viewport=VIEWPORT,
            locale='pt-BR',
            timezone_id='America/Sao_Paulo'
        )
        page = await context.new_page()

        while to_visit:
            current_url = to_visit.pop(0)
            
            if current_url in visited:
                continue
                
            logger.info(f"Coletando: {current_url}")
            
            try:
                await page.goto(current_url, timeout=TIMEOUT, wait_until='domcontentloaded')
                
                # Verificar idioma
                html = await page.content()
                if 'lang="pt-BR"' not in html and 'lang="pt"' not in html:
                    logger.info(f"Ignorando página não-PT: {current_url}")
                    continue
                
                # Baixar assets
                assets = await page.query_selector_all("link[href], script[src], img[src]")
                downloaded = {}
                
                for asset in assets:
                    attr = 'href' if await asset.get_attribute('href') else 'src'
                    url = await asset.get_attribute(attr)
                    if url:
                        orig_url, filename = await download_asset(page, url, current_url)
                        if orig_url and filename:
                            downloaded[orig_url] = filename
                
                # Processar HTML
                html = await page.content()
                for pattern, replacement in SUBSTITUTIONS:
                    html = re.sub(pattern, replacement, html)
                
                soup = BeautifulSoup(html, 'html.parser')
                
                # Atualizar links de assets
                for tag in soup.find_all(['link', 'script', 'img']):
                    attr = 'href' if tag.name == 'link' else 'src'
                    if tag.has_attr(attr) and tag[attr] in downloaded:
                        tag[attr] = f"/static/{downloaded[tag[attr]]}"
                
                # Salvar página
                parsed_url = urlparse(current_url)
                path = parsed_url.path.replace('/', '_').strip('_') or 'index'
                save_path = os.path.join(SAVE_DIR, f'{path}.html')
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                logger.info(f"Página salva: {save_path}")
                
                # Coletar novos links
                links = await page.query_selector_all('a[href]')
                for link in links:
                    href = await link.get_attribute('href')
                    full_url = urljoin(BASE_URL, href.split('#')[0].split('?')[0])
                    
                    if (
                        urlparse(full_url).netloc == urlparse(BASE_URL).netloc and
                        '/pt-BR/' in full_url and
                        full_url not in visited and
                        full_url not in to_visit and
                        not any(full_url.endswith(ext) for ext in ['.pdf', '.jpg', '.png'])
                    ):
                        to_visit.append(full_url)
                
                visited.add(current_url)
                
            except Exception as e:
                logger.error(f"Erro em {current_url}: {str(e)}")
                continue

        await context.close()
        await browser.close()
        logger.info("Scraping completo!")

async def main():
    logger.info("Iniciando scraping do site original...")
    await crawl_site()

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright
import os
import re
from urllib.parse import urljoin, urlparse
import mimetypes
import logging
from bs4 import BeautifulSoup
import random
from typing import Set, Dict

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
MAX_DEPTH = 2  # Profundidade máxima de navegação
MAX_PAGES = 50  # Número máximo de páginas a serem raspadas

# Substituições de dados sensíveis
SUBSTITUTIONS = [
    (r'\(\d{2}\)\s\d{4,5}-\d{4}', '(00) 0000-0000'),
    (r'\d{3}\.\d{3}\.\d{3}-\d{2}', '000.000.000-00'),
    (r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', '00.000.000/0000-00'),
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'contato@seudominio.com'),
    (r'\d{5}-\d{3}', '00000-000')
]

# Diretórios
SAVE_DIR = 'copart_clone/static'
STATIC_DIR = 'copart_clone/static'

# Controle de estado global
VISITED_URLS: Set[str] = set()
PAGES_MAPPING: Dict[str, str] = {}

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

async def scrape_index():
    """Faz scraping apenas da página index"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(
                    headless=False,
                    timeout=TIMEOUT
                )
                
                context = await browser.new_context(
                    user_agent=USER_AGENT,
                    viewport=VIEWPORT,
                    locale='pt-BR',
                    timezone_id='America/Sao_Paulo',
                    java_script_enabled=True,
                    ignore_https_errors=True
                )
                
                page = await context.new_page()
                
                try:
                    logger.info(f"Tentativa {attempt} para {BASE_URL}")
                    
                    await page.goto(BASE_URL, timeout=TIMEOUT, wait_until='domcontentloaded')
                    
                    title = await page.title()
                    if not title or "404" in title:
                        raise Exception("Página não encontrada ou inválida")
                    
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
                    
                    content = await page.content()
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    text = str(soup)
                    for pattern, replacement in SUBSTITUTIONS:
                        text = re.sub(pattern, replacement, text)
                    
                    soup = BeautifulSoup(text, 'html.parser')
                    for tag in soup.find_all(['link', 'script', 'img', 'source', 'video', 'audio', 'embed', 'object', 'iframe']):
                        attr = 'href' if tag.name == 'link' else ('src' if tag.has_attr('src') else 'data')
                        if tag.has_attr(attr):
                            original_url = tag[attr]
                            if original_url in downloaded_assets:
                                tag[attr] = f"/static/{downloaded_assets[original_url]}"
                    
                    os.makedirs(SAVE_DIR, exist_ok=True)
                    with open(os.path.join(SAVE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    logger.info(f"Página principal salva com sucesso em {os.path.join(SAVE_DIR, 'index.html')}")
                    return True
                    
                except Exception as e:
                    logger.error(f"Erro na tentativa {attempt}: {str(e)}")
                    if attempt < MAX_RETRIES:
                        await asyncio.sleep(RETRY_DELAY * attempt)
                    continue
                    
                finally:
                    await page.close()
                    await context.close()
                    await browser.close()
                    
        except Exception as e:
            logger.error(f"Erro geral na tentativa {attempt}: {str(e)}")
            continue
            
    return False

async def get_all_links(page, base_url: str) -> Set[str]:
    """Extrai todos os links válidos da página"""
    try:
        links = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('a[href]')).map(a => a.href);
        }''')
        
        valid_links = set()
        for link in links:
            if not link or link.startswith(('javascript:', 'mailto:', 'tel:', '#', 'data:')):
                continue
                
            parsed = urlparse(link)
            if not parsed.netloc or parsed.netloc == urlparse(base_url).netloc:
                normalized = urljoin(base_url, link)
                if normalized not in VISITED_URLS and len(VISITED_URLS) < MAX_PAGES:
                    valid_links.add(normalized)
                    
        return valid_links
    except Exception as e:
        logger.warning(f"Erro ao extrair links: {str(e)}")
        return set()

async def scrape_page(page, url: str, base_url: str, depth: int = 0):
    """Faz scraping de uma página específica"""
    if depth > MAX_DEPTH or url in VISITED_URLS or len(VISITED_URLS) >= MAX_PAGES:
        return
        
    VISITED_URLS.add(url)
    logger.info(f"Raspando: {url} (profundidade {depth})")
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            await page.goto(url, timeout=TIMEOUT, wait_until='domcontentloaded')
            
            title = await page.title()
            if not title or "404" in title:
                logger.warning(f"Página inválida: {url}")
                return
                
            # Baixar assets
            assets = await page.query_selector_all("""
                link[href], script[src], img[src], source[src], 
                video[src], audio[src], embed[src], object[data], iframe[src]
            """)
            
            downloaded_assets = {}
            for asset in assets:
                try:
                    src = await asset.get_attribute('href') or await asset.get_attribute('src') or await asset.get_attribute('data')
                    if src:
                        original_url, filename = await download_asset(page, src, base_url)
                        if original_url and filename:
                            downloaded_assets[original_url] = filename
                except Exception as e:
                    logger.warning(f"Erro ao processar asset: {str(e)}")
                    continue
            
            # Processar conteúdo
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            text = str(soup)
            for pattern, replacement in SUBSTITUTIONS:
                text = re.sub(pattern, replacement, text)
            
            soup = BeautifulSoup(text, 'html.parser')
            for tag in soup.find_all(['link', 'script', 'img', 'source', 'video', 'audio', 'embed', 'object', 'iframe']):
                attr = 'href' if tag.name == 'link' else ('src' if tag.has_attr('src') else 'data')
                if tag.has_attr(attr):
                    original_url = tag[attr]
                    if original_url in downloaded_assets:
                        tag[attr] = f"/static/{downloaded_assets[original_url]}"
            
            # Salvar o HTML
            path = urlparse(url).path
            if not path or path == '/':
                filename = 'index.html'
                filepath = os.path.join(SAVE_DIR, filename)
            else:
                path = path.rstrip('/')
                parts = path.split('/')
                filename = parts[-1] + '.html' if parts[-1] else 'index.html'
                dir_part = os.path.join(SAVE_DIR, *parts[:-1])
                os.makedirs(dir_part, exist_ok=True)
                filepath = os.path.join(dir_part, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                
            PAGES_MAPPING[url] = filepath
            logger.info(f"Página salva: {filepath}")
            
            # Obter links para páginas subsequentes
            if depth < MAX_DEPTH and len(VISITED_URLS) < MAX_PAGES:
                links = await get_all_links(page, base_url)
                for link in links:
                    await scrape_page(page, link, base_url, depth + 1)
            
            return
            
        except Exception as e:
            logger.error(f"Erro na tentativa {attempt} para {url}: {str(e)}")
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY * attempt)
            continue

async def scrape_full_site():
    """Faz scraping completo do site"""
    logger.info("Iniciando scraping completo do site...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            timeout=TIMEOUT
        )
        
        context = await browser.new_context(
            user_agent=USER_AGENT,
            viewport=VIEWPORT,
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
            java_script_enabled=True,
            ignore_https_errors=True
        )
        
        page = await context.new_page()
        
        try:
            await scrape_page(page, BASE_URL, BASE_URL)
            logger.info("Scraping completo concluído com sucesso!")
            return True
        except Exception as e:
            logger.error(f"Erro durante o scraping completo: {str(e)}")
            return False
        finally:
            await page.close()
            await context.close()
            await browser.close()

async def main():
    """Função principal"""
    logger.info("1. Iniciando scraping da página principal...")
    success = await scrape_index()
    
    if success:
        logger.info("2. Scraping da página principal concluído!")
        
        answer = input("Deseja raspar todo o site? (s/n): ").strip().lower()
        if answer == 's':
            await scrape_full_site()
    else:
        logger.error("Falha ao raspar a página principal")

if __name__ == "__main__":
    asyncio.run(main())

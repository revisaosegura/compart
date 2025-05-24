import asyncio
from playwright.async_api import async_playwright
import os
import re
from urllib.parse import urljoin, urlparse
import mimetypes
import hashlib
import logging
import shutil
from bs4 import BeautifulSoup

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configurações
BASE_URL = 'https://www.copart.com.br'
TARGET_DOMAIN = 'www.copartbr.com.br'
TARGET_URL = f'https://{TARGET_DOMAIN}'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
VIEWPORT = {'width': 1280, 'height': 1024}
TIMEOUT = 120000
STATIC_DIR = os.path.join('copart_clone', 'static')

# Substituições
SUBSTITUTIONS = [
    (r'\(\d{2}\)\s?\d{4,5}-\d{4}', '(11) 11 91471-9390'),
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'contato@copartbr.com.br'),
    (r'https?://(www\.)?copart\.com\.br', TARGET_URL),
    (r'//(www\.)?copart\.com\.br', f'//{TARGET_DOMAIN}'),
]

def sanitize_filename(url):
    parsed = urlparse(url)
    hash_digest = hashlib.md5(url.encode()).hexdigest()
    ext = os.path.splitext(parsed.path)[1] or '.bin'
    return f"{hash_digest}{ext}"

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

async def download_asset(page, url, base_url):
    if not is_valid_url(url):
        url = urljoin(base_url, url)

    if url.startswith(('data:', 'javascript:', 'mailto:', 'tel:')):
        return None, None

    try:
        response = await page.request.get(url)
        if response.status != 200:
            return None, None

        content = await response.body()
        content_type = response.headers.get('content-type', '')
        ext = mimetypes.guess_extension(content_type.split(';')[0]) or '.bin'
        filename = sanitize_filename(url)
        filepath = os.path.join(STATIC_DIR, filename)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            f.write(content)

        if ext in ['.css', '.js']:
            try:
                with open(filepath, 'r+', encoding='utf-8', errors='ignore') as f:
                    txt = f.read()
                    for pattern, repl in SUBSTITUTIONS:
                        txt = re.sub(pattern, repl, txt)
                    f.seek(0)
                    f.write(txt)
                    f.truncate()
            except:
                pass

        return url, filename
    except Exception as e:
        logger.warning(f"⚠️ Erro ao baixar {url}: {e}")
        return None, None

async def crawl_site():
    visited = set()
    to_visit = [BASE_URL]

    # Limpar diretório static antes de iniciar
    if os.path.exists(STATIC_DIR):
        shutil.rmtree(STATIC_DIR)
    os.makedirs(STATIC_DIR, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=USER_AGENT, viewport=VIEWPORT, locale='pt-BR')
        page = await context.new_page()

        while to_visit:
            current_url = to_visit.pop(0)
            if current_url in visited:
                continue

            try:
                logger.info(f"🌐 Visitando: {current_url}")
                await page.goto(current_url, timeout=TIMEOUT, wait_until='domcontentloaded')
                html = await page.content()

                for pattern, repl in SUBSTITUTIONS:
                    html = re.sub(pattern, repl, html)

                soup = BeautifulSoup(html, 'html.parser')
                downloaded = {}

                for tag in soup.find_all(['link', 'script', 'img']):
                    attr = 'href' if tag.name == 'link' else 'src'
                    if tag.has_attr(attr):
                        asset_url = tag[attr]
                        orig, local = await download_asset(page, asset_url, current_url)
                        if orig and local:
                            downloaded[orig] = local
                            tag[attr] = f"/static/{local}"

                for a in soup.find_all('a', href=True):
                    href = a['href']
                    full_url = urljoin(BASE_URL, href.split('#')[0].split('?')[0])
                    if BASE_URL in full_url and full_url not in visited and not full_url.endswith(('.pdf', '.jpg', '.png')):
                        to_visit.append(full_url)
                    a['href'] = href.replace(BASE_URL, TARGET_URL)

                final_path = os.path.join(STATIC_DIR, 'index.html') if current_url == BASE_URL else os.path.join(STATIC_DIR, sanitize_filename(current_url))

                with open(final_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))

                logger.info(f"✅ Salvo: {final_path}")
                visited.add(current_url)

            except Exception as e:
                logger.error(f"❌ Erro na URL {current_url}: {e}")

        await context.close()
        await browser.close()
        logger.info("✅ Espelhamento concluído com sucesso!")

async def main():
    logger.info("🚀 Iniciando espelhamento do site Copart...")
    await crawl_site()

if __name__ == "__main__":
    asyncio.run(main())

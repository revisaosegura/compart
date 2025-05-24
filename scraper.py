import os
import re
import asyncio
import shutil
import mimetypes
import logging
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# CONFIG
BASE_URL = "https://www.copart.com.br"
TARGET_URL = "https://copartbr.com.br"
STATIC_DIR = "copart_clone/static"
TIMEOUT = 30000
VIEWPORT = {"width": 1280, "height": 720}
PORTUGUESE_PATHS = ["/pt-br/", "/pt-BR/", "/pt/", "/content/br/pt", ".com.br", "/br/"]
MAX_WORKERS = 5
MAX_PAGES = 100

SUBSTITUTIONS = [
    (r'https://www\.copart\.com\.br', TARGET_URL),
    (r'https://copart\.com\.br', TARGET_URL),
    (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', 'contato@copartbr.com.br'),
    (r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}', '(11) 4000-0000'),
    (r'\d{3}\.\d{3}\.\d{3}-\d{2}', '000.000.000-00'),
    (r'/_Incapsula_Resource.*', '')
]

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("COPART_SCRAPER")

def sanitize_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path or path.endswith('/'):
        path += 'index'
    filename = path.replace('/', '_')
    if not filename.endswith('.html'):
        filename += '.html'
    return filename

def limpar_static():
    if os.path.exists(STATIC_DIR):
        shutil.rmtree(STATIC_DIR)
    os.makedirs(STATIC_DIR, exist_ok=True)

def is_portuguese_url(url):
    if not url:
        return False
    return any(segment in url.lower() for segment in PORTUGUESE_PATHS)

async def download_asset(page, url, base_url):
    try:
        if not url or any(url.startswith(s) for s in ('javascript:', 'data:', 'mailto:', 'tel:')):
            return None, None

        full_url = urljoin(base_url, url)
        if not full_url.startswith(("http://", "https://")) or 'Incapsula' in full_url:
            return None, None

        if not is_portuguese_url(full_url):
            return None, None

        response = await page.request.get(full_url, timeout=TIMEOUT)
        if response.status != 200:
            return None, None

        content = await response.body()
        content_type = response.headers.get("content-type", "")
        ext = mimetypes.guess_extension(content_type.split(';')[0]) or '.bin'
        filename = sanitize_filename(url)
        filepath = os.path.join(STATIC_DIR, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'wb') as f:
            f.write(content)

        if ext in ['.css', '.js', '.html']:
            try:
                with open(filepath, 'r+', encoding='utf-8', errors='ignore') as f:
                    txt = f.read()
                    for pattern, repl in SUBSTITUTIONS:
                        txt = re.sub(pattern, repl, txt)
                    f.seek(0)
                    f.write(txt)
                    f.truncate()
            except Exception as e:
                logger.warning(f"⚠️ Erro ao processar substituições em {filepath}: {e}")

        return url, filename
    except Exception as e:
        logger.warning(f"⚠️ Erro ao baixar {url}: {e}")
        return None, None

async def process_page(page, current_url, visited, to_visit, semaphore):
    async with semaphore:
        try:
            logger.info(f"🌐 Visitando: {current_url}")

            await page.goto(current_url, timeout=TIMEOUT, wait_until='networkidle')
            html = await page.content()

            if len(html) < 2000:
                raise Exception("Conteúdo insuficiente")

            soup = BeautifulSoup(html, 'html.parser')

            assets = []
            for tag in soup.find_all(['link', 'script', 'img', 'source']):
                attr = 'href' if tag.name == 'link' else 'src'
                if tag.has_attr(attr):
                    assets.append((tag, attr, tag[attr]))

            for tag, attr, asset_url in assets:
                orig, local = await download_asset(page, asset_url, current_url)
                if orig and local:
                    tag[attr] = f"/static/{local}"

            new_links = set()
            for a in soup.find_all('a', href=True):
                href = a['href']
                full_url = urljoin(BASE_URL, href.split('#')[0].split('?')[0])
                if (BASE_URL in full_url and full_url not in visited and
                    len(visited) < MAX_PAGES and
                    not full_url.endswith(('.pdf', '.jpg', '.png', '.zip', '.gif')) and
                    is_portuguese_url(full_url)):
                    new_links.add(full_url)
                a['href'] = href.replace(BASE_URL, TARGET_URL)

            to_visit.extend(new_links)

            filename = sanitize_filename(current_url)
            final_path = os.path.join(STATIC_DIR, filename)
            os.makedirs(os.path.dirname(final_path), exist_ok=True)
            with open(final_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            if current_url == BASE_URL:
                index_path = os.path.join(STATIC_DIR, "index.html")
                if os.path.abspath(final_path) != os.path.abspath(index_path):
                    shutil.copyfile(final_path, index_path)

            logger.info(f"✅ Salvo: {final_path} (Páginas restantes: {len(to_visit)})")
            visited.add(current_url)
        except Exception as e:
            logger.error(f"⛔ Erro na URL {current_url}: {e}")

async def crawl_site():
    visited = set()
    to_visit = [BASE_URL]
    semaphore = asyncio.Semaphore(MAX_WORKERS)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ],
            timeout=TIMEOUT
        )
        context = await browser.new_context(
            viewport=VIEWPORT,
            locale='pt-BR',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            java_script_enabled=True
        )
        page = await context.new_page()

        while to_visit and len(visited) < MAX_PAGES:
            current_url = to_visit.pop(0)
            if current_url in visited or not is_portuguese_url(current_url):
                continue
            await process_page(page, current_url, visited, to_visit, semaphore)

        await context.close()
        await browser.close()
        logger.info(f"🏁 Scraping finalizado. Páginas baixadas: {len(visited)}")

async def main():
    logger.info("🧹 Limpando pasta static...")
    limpar_static()
    logger.info("🚀 Iniciando espelhamento do Copart...")
    await crawl_site()

if __name__ == "__main__":
    asyncio.run(main())

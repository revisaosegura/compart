import asyncio
import os
import re
import shutil
import mimetypes
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright
import logging

# CONFIGURAÇÕES
BASE_URL = "https://www.copart.com.br"
TARGET_URL = "https://copartbr.com.br"
STATIC_DIR = "copart_clone/static"
TIMEOUT = 40000
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/90.0.4430.85 Safari/537.36"
VIEWPORT = {"width": 1280, "height": 720}
PORTUGUESE_PATHS = ["/pt-br/", "/pt-BR/", "/pt/", "/content/br/pt", ".com.br"]

SUBSTITUTIONS = [
    (r'https://www\.copart\.com\.br', TARGET_URL),
    (r'https://copart\.com\.br', TARGET_URL),
    (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', 'contato@copartbr.com.br'),
    (r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}', '(11) 4000-0000'),
    (r'\d{3}\.\d{3}\.\d{3}-\d{2}', '000.000.000-00')
]

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("COPART_SCRAPER")

def sanitize_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path or path.endswith('/'):
        path += 'index.html'
    if '.' not in os.path.basename(path):
        path += '.html'
    return path.replace('/', '_')

def limpar_static():
    if os.path.exists(STATIC_DIR):
        shutil.rmtree(STATIC_DIR)
    os.makedirs(STATIC_DIR, exist_ok=True)

def is_portuguese_url(url):
    url_lower = url.lower()
    return any(segment in url_lower for segment in PORTUGUESE_PATHS)

async def download_asset(page, url, base_url):
    try:
        full_url = urljoin(base_url, url)
        if not full_url.startswith("http") or 'Incapsula' in full_url:
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
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=USER_AGENT, viewport=VIEWPORT, locale='pt-BR')
        page = await context.new_page()

        while to_visit:
            current_url = to_visit.pop(0)
            if current_url in visited or not is_portuguese_url(current_url):
                continue
            try:
                logger.info(f"🌐 Visitando: {current_url}")
                await page.goto(current_url, timeout=TIMEOUT, wait_until='networkidle')
                await asyncio.sleep(1.5)
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
                    if BASE_URL in full_url and full_url not in visited and not full_url.endswith(('.pdf', '.jpg', '.png', '.zip')):
                        if is_portuguese_url(full_url):
                            to_visit.append(full_url)
                    a['href'] = href.replace(BASE_URL, TARGET_URL)

                filename = sanitize_filename(current_url)
                final_path = os.path.join(STATIC_DIR, filename)

                os.makedirs(os.path.dirname(final_path), exist_ok=True)
                with open(final_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))

                if current_url == BASE_URL:
                    index_path = os.path.join(STATIC_DIR, "index.html")
                    if os.path.abspath(final_path) != os.path.abspath(index_path):
                        shutil.copyfile(final_path, index_path)

                logger.info(f"✅ Salvo: {final_path}")
                visited.add(current_url)
            except Exception as e:
                logger.error(f"⛔ Erro na URL {current_url}: {e}")

        await context.close()
        await browser.close()
        logger.info("🏁 Scraping finalizado.")

async def main():
    logger.info("🧹 Limpando pasta static...")
    limpar_static()
    logger.info("🚀 Iniciando espelhamento do Copart...")
    await crawl_site()

if __name__ == "__main__":
    asyncio.run(main())

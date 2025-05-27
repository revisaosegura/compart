import asyncio
from playwright.async_api import async_playwright
import os
import re
from urllib.parse import urljoin, urlparse
import mimetypes
import logging
from bs4 import BeautifulSoup
import shutil
import random
from collections import deque

# Configurações
BASE_URL = 'https://www.copart.com.br'
TARGET_DOMAIN = 'copartbr.com.br'
TARGET_URL = f'https://{TARGET_DOMAIN}'
SAVE_DIR = 'copart_clone/static'
STATIC_DIR = 'copart_clone/static'
CONCURRENT_PAGES = 5
TIMEOUT = 60000
VIEWPORT = {'width': 1280, 'height': 1024}
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
]

KEEP_ORIGINAL_SUBDOMAINS = ['library', 'brimages']
EXTERNAL_DOMAINS_TO_KEEP = ['fonts.gstatic.com', 'cdn.cookielaw.org', 'fonts.googleapis.com']

SUBSTITUTIONS = [
    (r'\(\d{2}\)\s?\d{4,5}-\d{4}', '(11) 11 91471-9390'),
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 'contato@copartbr.com.br'),
    (r'https?://(www\.)?copart\.com\.br', TARGET_URL),
    (r'//(www\.)?copart\.com\.br', f'//{TARGET_DOMAIN}'),
    (r'www\.copart\.com\.br', TARGET_DOMAIN),
    (r'copart\.com\.br', TARGET_DOMAIN),
]

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('scraper.log', encoding='utf-8'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def should_keep_original(url):
    parsed = urlparse(url)
    if not parsed.netloc:
        return False
    if any(parsed.netloc.startswith(f"{sub}.") for sub in KEEP_ORIGINAL_SUBDOMAINS):
        return True
    if any(domain in parsed.netloc for domain in EXTERNAL_DOMAINS_TO_KEEP):
        return True
    return False

def apply_substitutions(text):
    for pattern, repl in SUBSTITUTIONS:
        text = re.sub(pattern, repl, text)
    return text

def sanitize_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path or path == '':
        return 'index.html'
    ext = os.path.splitext(path)[1]
    if not ext or ext.lower() not in ['.html', '.htm']:
        ext = '.html'
    safe_path = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', path)
    return safe_path[:100] + ext

async def download_asset(page, url, base_url):
    if not is_valid_url(url):
        url = urljoin(base_url, url)
    if url.startswith(('data:', 'javascript:', 'mailto:', 'tel:')) or should_keep_original(url):
        return url, None
    try:
        response = await page.request.get(url, timeout=TIMEOUT)
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
        if ext in ['.css', '.js', '.html']:
            try:
                with open(filepath, 'r+', encoding='utf-8', errors='ignore') as f:
                    txt = apply_substitutions(f.read())
                    f.seek(0)
                    f.write(txt)
                    f.truncate()
            except:
                pass
        return url, filename
    except:
        return None, None

async def process_url(context, current_url, visited, to_visit):
    page = await context.new_page()
    try:
        logger.info(f"🔗 Visitando: {current_url}")
        await page.goto(current_url, timeout=TIMEOUT, wait_until='networkidle')
        await page.wait_for_selector('body', timeout=TIMEOUT)
        html = await page.content()
        if '<body' not in html or len(html.strip()) < 1000:
            html = "<html><body>" + await page.inner_html('body') + "</body></html>"

        html = apply_substitutions(html)
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.find_all(True):
            for attr in list(tag.attrs):
                if attr.startswith(('ng-', 'uib-', 'data-ng-')) or '{{' in str(tag[attr]):
                    del tag[attr]

        asset_tags = [tag for tag in soup.find_all(['link', 'script', 'img', 'source'])]
        asset_tasks = []
        for tag in asset_tags:
            attr = 'href' if tag.name == 'link' else 'src'
            if tag.has_attr(attr) and not should_keep_original(tag[attr]):
                asset_tasks.append(download_asset(page, tag[attr], current_url))

        asset_results = await asyncio.gather(*asset_tasks)
        idx = 0
        for tag in asset_tags:
            attr = 'href' if tag.name == 'link' else 'src'
            if tag.has_attr(attr) and not should_keep_original(tag[attr]):
                orig, local = asset_results[idx]
                if orig and local:
                    tag[attr] = f"/static/{local}"
                idx += 1

        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(BASE_URL, href.split('#')[0].split('?')[0])
            if (BASE_URL in full_url and full_url not in visited and full_url not in to_visit
                    and not full_url.endswith(('.pdf', '.jpg', '.png', '.jpeg', '.gif', '.zip'))):
                to_visit.append(full_url)
            a['href'] = apply_substitutions(href)

        filename = sanitize_filename(current_url)
        final_path = os.path.join(SAVE_DIR, filename)
        os.makedirs(os.path.dirname(final_path), exist_ok=True)
        with open(final_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        logger.info(f"✅ Salvo: {final_path}")
        visited.add(current_url)
    except Exception as e:
        logger.error(f"❌ Erro em {current_url}: {e}")
    finally:
        await page.close()

async def crawl_site():
    visited = set()
    to_visit = deque([BASE_URL])

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled'])
        context = await browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            viewport=VIEWPORT,
            locale='pt-BR',
            bypass_csp=True,
            ignore_https_errors=True,
        )
        await context.add_init_script("""
            delete navigator.__proto__.webdriver;
            window.navigator.chrome = { runtime: {}, };
            Object.defineProperty(navigator, 'languages', {
                get: () => ['pt-BR', 'pt']
            });
        """)

        sem = asyncio.Semaphore(CONCURRENT_PAGES)

        async def worker():
            while True:
                try:
                    url = to_visit.popleft()
                except IndexError:
                    return
                if url in visited:
                    continue
                async with sem:
                    await process_url(context, url, visited, to_visit)

        workers = [asyncio.create_task(worker()) for _ in range(CONCURRENT_PAGES)]
        await asyncio.gather(*workers)
        await context.close()
        await browser.close()
        logger.info("🎉 Scraping completo.")

def limpar():
    logger.info("🧹 Limpando diretórios...")
    shutil.rmtree(SAVE_DIR, ignore_errors=True)
    shutil.rmtree(STATIC_DIR, ignore_errors=True)

async def main():
    if '--clean' in os.sys.argv:
        limpar()
    os.makedirs(SAVE_DIR, exist_ok=True)
    os.makedirs(STATIC_DIR, exist_ok=True)
    await crawl_site()

if __name__ == '__main__':
    asyncio.run(main())

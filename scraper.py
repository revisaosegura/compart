# scraper.py
import os, re, time, urllib.parse
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.copart.com.br"
TEMPLATE_DIR = "copart_clone/templates/copart"
STATIC_DIR = "copart_clone/static"

def sanitize_filename(url_path):
    # Remove query params e caracteres inválidos para Windows
    filename = url_path.split("?")[0]
    filename = filename.replace(":", "_").replace("&", "_").replace("=", "_")
    return filename

def baixar_arquivo(url, destino):
    try:
        path_sanitizado = sanitize_filename(destino)
        os.makedirs(os.path.dirname(path_sanitizado), exist_ok=True)
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(path_sanitizado, "wb") as f:
                f.write(response.content)
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")

def proteger_template(html):
    # Protege {{ }} com {% raw %} no Django
    html = re.sub(r"{{(.*?)}}", r"{% raw %}{{\1}}{% endraw %}", html)
    return html

def salvar_site():
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    os.makedirs(STATIC_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, timeout=60000)
        time.sleep(5)
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup.find_all(["script", "link", "img"]):
            attr = "src" if tag.name != "link" else "href"
            url = tag.get(attr)
            if url and not url.startswith("http") and not url.startswith("data"):
                full_url = urllib.parse.urljoin(BASE_URL, url)
                local_path = os.path.join(STATIC_DIR, sanitize_filename(url.lstrip("/")))
                baixar_arquivo(full_url, local_path)
                tag[attr] = f"/static/copart/{url.lstrip('/')}"

        html_final = proteger_template(str(soup))
        with open(os.path.join(TEMPLATE_DIR, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_final)
        browser.close()

if __name__ == "__main__":
    salvar_site()
    print("[✓] Site espelhado com sucesso.")

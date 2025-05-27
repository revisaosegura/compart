import os
import re
import time
import urllib.parse
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.copart.com.br"
PAGES_TO_CLONE = [
    "/",  # home
    "/vehicle-search",
    "/locations",
    "/members",
    "/auctionCalendar",
    "/lotSearchResults",
    "/vehicleFinderSearch"
]

TEMPLATE_DIR = "templates/copart"
STATIC_DIR = "static/copart"

def sanitize_filename(url_path):
    # Remove parâmetros e caracteres inválidos
    filename = url_path.split("?")[0]
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename

def baixar_arquivo(url, destino):
    if "Incapsula" in url or "nly-Fathere" in url:
        return  # ignora arquivos inúteis
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as f:
                f.write(response.content)
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")

def proteger_template(html):
    html = re.sub(r"{{(.*?)}}", r"{% raw %}{{\1}}{% endraw %}", html)
    return html

def processar_pagina(page, url_path):
    page.goto(BASE_URL + url_path, timeout=60000)
    time.sleep(5)
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    # baixar e corrigir assets
    for tag in soup.find_all(["script", "link", "img"]):
        attr = "src" if tag.name != "link" else "href"
        url = tag.get(attr)
        if url and not url.startswith("http") and not url.startswith("data"):
            full_url = urllib.parse.urljoin(BASE_URL, url)
            local_path = os.path.join(STATIC_DIR, sanitize_filename(url.lstrip("/")))
            baixar_arquivo(full_url, local_path)
            tag[attr] = "/static/copart/" + sanitize_filename(url.lstrip("/"))

    html_final = proteger_template(str(soup))

    # salvar HTML
    slug = url_path.strip("/").replace("/", "_") or "index"
    html_path = os.path.join(TEMPLATE_DIR, f"{slug}.html")
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"[✓] Página salva: {url_path} → {html_path}")

def salvar_site():
    os.makedirs(STATIC_DIR, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for url_path in PAGES_TO_CLONE:
            try:
                processar_pagina(page, url_path)
            except Exception as e:
                print(f"[!] Erro na página {url_path}: {e}")
        browser.close()

if __name__ == "__main__":
    salvar_site()

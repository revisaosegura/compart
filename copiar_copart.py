import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

BASE_URL = "https://www.copart.com.br"
OUTPUT_DIR = "copart_site"

visited = set()

def is_valid_url(url):
    return url.startswith(BASE_URL)

def save_file(url, path):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(f"[!] Falhou ao salvar {url} -> {e}")

def sanitize_path(url):
    parts = urlparse(url)
    path = parts.path
    if path.endswith("/"):
        path += "index.html"
    elif '.' not in os.path.basename(path):
        path += "/index.html"
    return os.path.join(OUTPUT_DIR, path.lstrip("/"))

def scrape_page(url):
    if url in visited:
        return
    visited.add(url)

    print(f"📄 Baixando: {url}")
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[x] Erro ao acessar {url}: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    page_path = sanitize_path(url)
    os.makedirs(os.path.dirname(page_path), exist_ok=True)

    for tag in soup.find_all(["a", "link", "script", "img"]):
        attr = "href" if tag.name in ["a", "link"] else "src"
        link = tag.get(attr)
        if not link:
            continue
        full_url = urljoin(url, link)
        if not full_url.startswith("http"):
            continue
        if is_valid_url(full_url):
            scrape_page(full_url)
        if BASE_URL in full_url:
            rel_path = sanitize_path(full_url)
            tag[attr] = os.path.relpath(rel_path, os.path.dirname(page_path))
            save_file(full_url, rel_path)

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

# Início do processo
print("🚀 Iniciando cópia do site Copart...")
scrape_page(BASE_URL)
print("✅ Finalizado! Arquivos salvos em:", OUTPUT_DIR)

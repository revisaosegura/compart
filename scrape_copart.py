
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

BASE_URL = "https://www.copart.com.br"
OUTPUT_DIR = "templates/copart"
MAX_DEPTH = 2

visited = set()

def save_page(url, output_path):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[✔] Página salva: {output_path}")
    except Exception as e:
        print(f"[✘] Erro ao acessar {url}: {e}")

def crawl(url, depth=0):
    if depth > MAX_DEPTH or url in visited:
        return
    visited.add(url)
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "index"
    filename = path.replace("/", "_") + ".html"
    output_path = os.path.join(OUTPUT_DIR, filename)
    save_page(url, output_path)

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            next_url = urljoin(url, href)
            if urlparse(next_url).netloc == urlparse(BASE_URL).netloc:
                crawl(next_url, depth + 1)
    except Exception as e:
        print(f"[✘] Falha ao extrair links de {url}: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando cópia recursiva do site Copart...")
    crawl(BASE_URL)
    print("✅ Finalizado! Arquivos salvos em:", OUTPUT_DIR)

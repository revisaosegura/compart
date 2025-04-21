import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

base_url = "https://www.copart.com.br"
pages = [
    "",  # homepage
    "lotes", "sobre", "como-funciona", "vistorias", "vendedores",
    "fale-conosco", "seguranca"
]

TEMPLATES_DIR = os.path.join("copart_clone", "templates", "copart")
os.makedirs(TEMPLATES_DIR, exist_ok=True)

def start_scraping():
    print("🚀 Iniciando cópia do site Copart...")

    for page in tqdm(pages, desc="Copiando páginas"):
        url = f"{base_url}/{page}" if page else base_url
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Salva com nome index.html se for homepage
            filename = "index.html" if page == "" else f"{page}.html"

            with open(os.path.join(TEMPLATES_DIR, filename), "w", encoding="utf-8") as f:
                f.write(str(soup))
        else:
            print(f"❌ Falha ao acessar: {url}")

    print("✅ Scraping finalizado.")

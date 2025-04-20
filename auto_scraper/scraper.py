# auto_scraper/scraper.py

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

BASE_URL = "https://www.copart.com.br"
SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates/copart")

def baixar_pagina(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(response.text)
    except Exception as e:
        print(f"❌ Erro ao baixar {url}: {e}")

def start_scraping():
    print("🚀 Iniciando cópia do site Copart...")

    paginas = [
        "",
        "veiculos", 
        "como-funciona",
        "lotes", 
        "vender-carro", 
        "faq", 
        "sobre-nos", 
        "fale-conosco"
    ]

    for pagina in tqdm(paginas, desc="Copiando páginas"):
        url = urljoin(BASE_URL + "/", pagina)
        nome_arquivo = "index.html" if pagina == "" else f"{pagina}.html"
        caminho = os.path.join(SAVE_DIR, nome_arquivo)
        baixar_pagina(url, caminho)

    print("✅ Scraping finalizado.")

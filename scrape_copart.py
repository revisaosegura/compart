
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "https://www.copart.com.br"
OUTPUT_DIR = "vehicles/templates/vehicles"

# Criar a pasta de destino se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Visitar a página principal
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Salvar a página principal
with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Encontrar todos os links internos (mesmo domínio)
internal_links = set()
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.startswith("/") or BASE_URL in href:
        full_url = urljoin(BASE_URL, href)
        parsed = urlparse(full_url)
        clean_path = parsed.path.strip("/")
        if clean_path and not clean_path.startswith("javascript") and '.' not in clean_path:
            internal_links.add((clean_path, full_url))

# Baixar e salvar cada página
for path, full_url in internal_links:
    try:
        resp = requests.get(full_url)
        html = resp.text
        file_name = f"{path.replace('/', '_')}.html"

        with open(os.path.join(OUTPUT_DIR, file_name), "w", encoding="utf-8") as f:
            f.write(html)

        print(f"[✔] Página salva: {file_name}")
    except Exception as e:
        print(f"[✘] Erro ao acessar {full_url}: {e}")

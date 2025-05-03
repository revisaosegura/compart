import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://www.copart.com.br"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static_site")

def scrape_site():
    session = requests.Session()
    urls_to_scrape = [BASE_URL]
    scraped_urls = set()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    while urls_to_scrape:
        url = urls_to_scrape.pop(0)
        if url in scraped_urls:
            continue

        try:
            response = session.get(url, timeout=10)
            if response.status_code != 200:
                continue
        except Exception:
            continue

        parsed_url = urlparse(url)
        local_path = parsed_url.path.lstrip("/")
        if not local_path or local_path.endswith("/"):
            local_path += "index.html"
        save_path = os.path.join(OUTPUT_DIR, local_path)

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        # Atualiza os links locais
        for tag in soup.find_all(["a", "link", "script", "img"]):
            attr = "href" if tag.name in ["a", "link"] else "src"
            if tag.has_attr(attr):
                file_url = urljoin(url, tag[attr])
                parsed_file_url = urlparse(file_url)

                if parsed_file_url.netloc == urlparse(BASE_URL).netloc:
                    file_local_path = parsed_file_url.path.lstrip("/")
                    if not file_local_path or file_local_path.endswith("/"):
                        file_local_path += "index.html"
                    tag[attr] = f"/static_site/{file_local_path}"

                    # Baixar o arquivo se ainda não foi baixado
                    full_file_path = os.path.join(OUTPUT_DIR, file_local_path)
                    if not os.path.exists(full_file_path):
                        try:
                            file_response = session.get(file_url, timeout=10)
                            if file_response.status_code == 200:
                                os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
                                with open(full_file_path, "wb") as f:
                                    f.write(file_response.content)
                        except Exception:
                            pass

                # Adicionar novas páginas para scrape
                if tag.name == "a" and parsed_file_url.netloc == urlparse(BASE_URL).netloc:
                    if file_url not in scraped_urls:
                        urls_to_scrape.append(file_url)

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(str(soup))

        scraped_urls.add(url)
        time.sleep(1)  # Evitar banimento por scraping rápido

def start_scraping():
    print("Iniciando scraping da Copart...")
    pass


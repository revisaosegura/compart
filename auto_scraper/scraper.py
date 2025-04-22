import os
import time
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from tqdm import tqdm
from pathlib import Path

PAGINAS = [
    "https://www.copart.com.br/",
]

TEMPLATE_DIR = os.path.join("copart_clone", "templates", "copart")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

def limpar_templates_antigos():
    print("🧹 Limpando templates antigos...")
    pasta_templates = "copart_clone/templates/copart"
    if os.path.exists(pasta_templates):
        shutil.rmtree(pasta_templates)
    os.makedirs(pasta_templates)
    print("🧹 Templates antigos removidos.")


def start_scraping():
    urls = [
        "https://www.copart.com.br/",
        # Adicione mais URLs se quiser expandir a cópia
    ]

    pasta_destino = "copart_clone/templates/copart"

    print("🚀 Iniciando cópia do site Copart com Selenium...")

    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")

    driver = None
    try:
        driver = uc.Chrome(options=options)

        for url in tqdm(urls, desc="Copiando páginas"):
            try:
                driver.get(url)
                time.sleep(2)

                html = driver.page_source
                nome_arquivo = url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
                if not nome_arquivo:
                    nome_arquivo = "index"
                caminho = os.path.join(pasta_destino, f"{nome_arquivo}.html")
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(html)

            except Exception as e:
                print(f"❌ Erro ao copiar {url}: {e}")

        print("✅ Templates atualizados com sucesso.")

    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass  # Silencia erro WinError 6 no Windows


    # 🧠 Substituir blocos JS que causam erro de template
    template_dir = Path("copart_clone/templates/copart")
    for file in template_dir.rglob("*.html"):
        content = file.read_text(encoding="utf-8")
        if "{{" in content and "}}" in content:
            updated = content.replace("{{", "{% raw %}{{").replace("}}", "}}{% endraw %}")
            file.write_text(updated, encoding="utf-8")

    print("✅ Todos os templates HTML atualizados com blocos {% raw %} para evitar erros do Django.")

if not list(Path("copart_clone/templates/copart").glob("*.html")):
    print("❌ Nenhum template foi salvo. Algo deu errado no scraping.")
else:
    print("✅ Templates salvos com sucesso.")

import os
import time
from pathlib import Path
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

# Caminho base do projeto Django
BASE_DIR = Path(__file__).resolve().parent.parent

URLS = [
    "https://www.copart.com.br/",
    # Adicione outras URLs importantes que deseja capturar aqui
]

TEMPLATE_PATH = Path("copart_clone/templates/copart")


def limpar_templates_antigos():
    print("🧹 Removendo templates antigos...")
    pasta = os.path.join(BASE_DIR, "copart_clone", "templates", "copart")
    if os.path.exists(pasta):
        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".html"):
                os.remove(os.path.join(pasta, arquivo))
    print("🧹 Templates antigos removidos.")
    

def extrair_html_renderizado(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return driver.page_source
    except Exception as e:
        print(f"❌ Erro ao copiar {url}: {e}")
        return None

def salvar_template(nome_arquivo, conteudo):
    save_path = os.path.join(BASE_DIR, "copart_clone", "templates", "copart")
    os.makedirs(save_path, exist_ok=True)

    # Caminho fixo para salvar sempre como index.html
    filename = "index.html"
    filepath = os.path.join(save_path, filename)

    # Adiciona {% verbatim %} automaticamente ao redor de blocos com {{ }}
    if "{{" in conteudo and "}}" in conteudo:
        conteudo = conteudo.replace("{{", "{% verbatim %}{{").replace("}}", "}}{% endverbatim %}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print("✅ Template salvo como index.html.")

def start_scraping():
    print("📡 Iniciando cópia dos templates com Selenium...")

    # Configurações do navegador
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = uc.Chrome(options=options)

    limpar_templates_antigos()

    sucesso = False

    for url in tqdm(URLS, desc="Copiando páginas"):
        html = extrair_html_renderizado(driver, url)
        if html:
            salvar_template("index.html", html)
            sucesso = True

    driver.quit()

    if sucesso:
        print("✅ Todos os templates HTML atualizados com blocos {% verbatim %} para evitar erros do Django.")
        print("✅ Templates salvos com sucesso.")
    else:
        print("❌ Nenhum template foi salvo. Algo deu errado no scraping.")

# Garante que o driver será fechado mesmo com erro
try:
    driver.quit()
except Exception:
    pass

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from tqdm import tqdm

PAGINAS = [
    "https://www.copart.com.br/",
]

TEMPLATE_DIR = os.path.join("copart_clone", "templates", "copart")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

def start_scraping():
    print("🚀 Iniciando cópia do site Copart com Selenium...")

    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")

    driver = uc.Chrome(options=options)

    for url in tqdm(PAGINAS, desc="Copiando páginas"):
        try:
            driver.get(url)
            driver.implicitly_wait(10)
            html = driver.page_source

            nome_arquivo = url.split("/")[-2] if url.rstrip("/").endswith("veiculos") else "index"
            caminho = os.path.join(TEMPLATE_DIR, f"{nome_arquivo}.html")

            soup = BeautifulSoup(html, "html.parser")

            # Remove scripts e iframes
            for tag in soup(["script", "iframe"]):
                tag.decompose()

            with open(caminho, "w", encoding="utf-8") as f:
                f.write(str(soup))

        except Exception as e:
            print(f"❌ Erro ao copiar {url}: {e}")

    try:
        driver.quit()
    except Exception:
        pass

    print("✅ Templates atualizados com sucesso.")

def limpar_templates_antigos(pasta_templates="copart_clone/templates/copart"):
    import os
    import glob
    import shutil

    print("🧹 Limpando templates antigos...")
    arquivos_html = glob.glob(os.path.join(pasta_templates, "*.html"))
    for arquivo in arquivos_html:
        os.remove(arquivo)

    pastas = [d for d in os.listdir(pasta_templates) if os.path.isdir(os.path.join(pasta_templates, d))]
    for pasta in pastas:
        shutil.rmtree(os.path.join(pasta_templates, pasta))

    print("🧹 Templates antigos removidos.")

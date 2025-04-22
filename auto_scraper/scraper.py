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

def limpar_templates_antigos(pasta_templates):
    print("🧹 Limpando e corrigindo templates antigos...")

    for root, dirs, files in os.walk(pasta_templates):
        for file in files:
            if file.endswith(".html"):
                caminho = os.path.join(root, file)
                with open(caminho, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')

                # Corrige {{ objeto['chave'] }} que quebra no Django
                for tag in soup.find_all(string=True):
                    if "{{" in tag and "['" in tag:
                        tag.replace_with(tag.replace("{{", "").replace("}}", "").split("[")[0].strip())

                # Protege com {% raw %}
                conteudo = str(soup)
                conteudo = conteudo.replace("{{", "{% raw %}{{").replace("}}", "}}{% endraw %}")

                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)

    print("🧼 Templates corrigidos com sucesso.")

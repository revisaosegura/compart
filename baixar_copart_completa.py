import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Base do projeto Django
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "copart_clone", "templates", "copart")
STATIC_JS_DIR = os.path.join(BASE_DIR, "copart_clone", "static", "copart", "js")

# URL principal
URL = "https://www.copart.com.br/"

# Apaga HTML antigo
if os.path.exists(os.path.join(TEMPLATE_DIR, "index.html")):
    os.remove(os.path.join(TEMPLATE_DIR, "index.html"))
    print("🧹 index.html anterior removido.")

# Cria diretórios se não existirem
os.makedirs(TEMPLATE_DIR, exist_ok=True)
os.makedirs(STATIC_JS_DIR, exist_ok=True)

print("📥 Baixando HTML...")
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

print("🔧 Processando scripts externos...")
scripts = soup.find_all("script", src=True)

for script in scripts:
    src = script["src"]
    if src.startswith("http"):
        script_url = src
        filename = os.path.basename(urlparse(script_url).path)
        local_path = os.path.join(STATIC_JS_DIR, filename)
        try:
            r = requests.get(script_url)
            r.raise_for_status()
            with open(local_path, "wb") as f:
                f.write(r.content)
            print(f"✅ Script salvo: {filename}")
            # Atualiza o caminho no HTML
            script["src"] = f"/static/copart/js/{filename}"
        except Exception as e:
            print(f"❌ Falha ao baixar {script_url}: {e}")

# Salva o novo index.html
index_path = os.path.join(TEMPLATE_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("✅ index.html atualizado com scripts locais!")
print("🚀 Espelho pronto para rodar offline.")



import os
import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.copart.com.br/"
TEMPLATE_PATH = "copart_clone/templates/copart/index.html"

def proteger_variaveis(html):
    html = re.sub(r"({{.*?}})", r"{% raw %}\1{% endraw %}", html)
    html = re.sub(r"(::locale\\.messages\[.*?\])", r"{% raw %}\1{% endraw %}", html)
    return html

def baixar_e_salvar():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print("📥 Baixando HTML da Copart...")
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Erro ao baixar o HTML: {e}")
        return

    html = response.text
    html_protegido = proteger_variaveis(html)

    os.makedirs(os.path.dirname(TEMPLATE_PATH), exist_ok=True)

    with open(TEMPLATE_PATH, "w", encoding="utf-8") as f:
        f.write(html_protegido)

    print(f"✅ index.html atualizado e protegido salvo em {TEMPLATE_PATH}")

if __name__ == "__main__":
    baixar_e_salvar()

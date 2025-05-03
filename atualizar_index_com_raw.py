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

def adicionar_load_static(html):
    # Garante que o {% load static %} venha logo após a primeira tag <html> ou <!DOCTYPE>
    lines = html.splitlines()
    for i, line in enumerate(lines):
        if "<html" in line or "<!DOCTYPE" in line:
            # Insere após essa linha
            lines.insert(i + 1, "{% load static %}")
            break
    return "\n".join(lines)

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
    html = adicionar_load_static(html)
    html = proteger_variaveis(html)

    os.makedirs(os.path.dirname(TEMPLATE_PATH), exist_ok=True)

    with open(TEMPLATE_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ index.html atualizado e protegido salvo em {TEMPLATE_PATH}")

if __name__ == "__main__":
    baixar_e_salvar()

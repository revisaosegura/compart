import requests
from bs4 import BeautifulSoup

url = "https://www.copart.com.br/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    # Exibe o HTML da resposta (pra vermos se veio conteúdo mesmo ou só scripts)
    print(soup.prettify()[:2000])  # mostra os 2000 primeiros caracteres
else:
    print("Erro ao acessar:", resposta.status_code)

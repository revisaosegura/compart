import requests

# URL da API pública da Copart que retorna dados dos veículos em JSON
url = "https://www.copart.com/public/lots/search?free=true&query=&size=10&page=1"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for item in data["data"]["results"]:
        lot = item.get("lotNumberStr")
        marca = item.get("make", "Desconhecido")
        modelo = item.get("model", "Desconhecido")
        lance = item.get("currentBid", "Sem lance")
        ano = item.get("year", "N/A")
        local = item.get("location", {}).get("name", "Desconhecido")
        
        print(f"[{lot}] {marca} {modelo} ({ano}) - Lance: {lance} - Local: {local}")
else:
    print("Erro ao acessar a API:", response.status_code)

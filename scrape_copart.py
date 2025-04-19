from playwright.sync_api import sync_playwright

def coletar_veiculos_copart():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        
        # Acessar página principal de leilões (pode ajustar conforme sua necessidade)
        pagina.goto("https://www.copart.com.br/")
        pagina.wait_for_timeout(8000)  # Espera o conteúdo carregar

        # Captura o conteúdo HTML depois do carregamento do JS
        html = pagina.content()
        print(html[:2000])  # Mostra os 2000 primeiros caracteres

        navegador.close()

# Chamar a função
coletar_veiculos_copart()

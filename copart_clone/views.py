import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from auto_scraper.scraper import start_scraping

PAGES_DIR = os.path.join(settings.BASE_DIR, 'copart_clone/templates/copart')

def serve_template(request, path="index.html"):
    file_path = os.path.join(settings.TEMPLATES[0]["DIRS"][0], path)
    if not os.path.isfile(file_path):
        raise Http404("Página não encontrada")
    with open(file_path, encoding="utf-8") as f:
        return HttpResponse(f.read())

def home(request):
    # Executa o scraping ao acessar a home
    start_scraping()
    return render(request, "copart/index.html")

def run_scraper(request):
    print("🚀 Iniciando cópia do site Copart...")
    start_scraping()
    print("✅ Scraping finalizado.")
    return render(request, "copart/index.html")

def render_pagina(request, pagina):
    template_path = f"copart/{pagina}.html"
    if os.path.exists(os.path.join(PAGES_DIR, f"{pagina}.html")):
        return render(request, template_path)
    else:
        raise Http404("Página não encontrada.")

def lista_paginas(request):
    arquivos = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]
    return render(request, 'lista_paginas.html', {'arquivos': arquivos})

def ver_pagina(request, nome_arquivo):
    caminho = os.path.join(PAGES_DIR, nome_arquivo)
    if not os.path.isfile(caminho):
        return render(request, 'pagina_nao_encontrada.html')

    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    return render(request, 'pagina_visualizacao.html', {'conteudo': conteudo})

def homepage(request):
    return render(request, "copart/index.html")

def sobre(request):
    return render(request, "copart/sobre.html")

def lotes(request):
    return render(request, "copart/lotes.html")

def contato(request):
    return render(request, "copart/contato.html")

def ajuda(request):
    return render(request, "copart/ajuda.html")

def termos(request):
    return render(request, "copart/termos.html")

def privacidade(request):
    return render(request, "copart/privacidade.html")

def login(request):
    return render(request, "copart/login.html")

def dynamic_template_view(request, page="index"):
    template_name = f"copart/{page}.html"
    template_path = os.path.join(PAGES_DIR, f"{page}.html")

    if os.path.exists(template_path):
        return render(request, template_name)
    else:
        raise Http404("Página não encontrada.")

def index(request):
    return render(request, 'copart/index.html')

def render_template(request, template_name):
    template_path = f"copart/{template_name}"
    if os.path.exists(os.path.join(PAGES_DIR, template_name)):
        return render(request, template_path)
    else:
        return render(request, "copart/index.html")  # fallback

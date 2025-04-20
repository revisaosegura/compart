import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from auto_scraper.scraper import start_scraping

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
    return render(request, "index.html")

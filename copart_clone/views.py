import subprocess
import sys
import os
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings
from .models import Cadastro
from django.shortcuts import render, redirect
from .forms import CadastroForm

def _serve_static_html(filename: str):
    """Helper to return a static HTML file without template rendering."""
    base = os.path.join(settings.BASE_DIR, 'copart_clone', 'templates', 'copart')
    path = os.path.join(base, filename)
    if not os.path.exists(path):
        raise Http404
    with open(path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())


def home(request):
<<<<<<< HEAD
    return _serve_static_html('index.html')
=======
    return render(request, 'copart/index.html')
>>>>>>> f419c2e9050c98a7117cabca7a287923894cdad6

def page(request, name):
    return _serve_static_html(f'{name}.html')

def cadastro_view(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = CadastroForm()
    return render(request, "cadastro.html", {"form": form})

def agendar_scraper_view(request, pk):
    cadastro = Cadastro.objects.get(pk=pk)

    try:
        # Caminho absoluto para o script scraper.py
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        scraper_path = os.path.join(base_dir, 'scraper.py')

        # Executa o script
        subprocess.Popen([sys.executable, scraper_path])

        messages.success(request, f"Scraper agendado com sucesso para: {cadastro.nome}")
    except Exception as e:
        messages.error(request, f"Erro ao agendar scraper: {str(e)}")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))

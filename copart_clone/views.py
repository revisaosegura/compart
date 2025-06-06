import subprocess
import sys
import os
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Cadastro
from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.shortcuts import render

def home(request):
    return render(request, "copart/index.html")

def page(request, name):
    return render(request, f"copart/{name}.html")

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

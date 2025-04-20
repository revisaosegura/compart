from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'copart/index.html')

def serve_template(request, template):
    try:
        return render(request, f'copart/{template}')
    except:
        return HttpResponseNotFound('Página não encontrada')

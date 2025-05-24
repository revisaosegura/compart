from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

def home_redirect(request):
    """Redireciona para a página inicial do clone"""
    index_path = os.path.join('copart_clone/static', 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='text/html')
    return HttpResponse("Página inicial não encontrada", status=404)

def serve_cloned_page(request, path):
    """Serve páginas do site clonado"""
    if not path or path == '/':
        path = 'index.html'
    elif path.endswith('/'):
        path = path.rstrip('/') + '.html'
    elif '.' not in os.path.basename(path):
        path += '.html'
        
    template_path = os.path.join('copart_clone/static', path)
    
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            content_type = 'text/html' if path.endswith('.html') else 'text/plain'
            return HttpResponse(content, content_type=content_type)
    
    return HttpResponse("Página não encontrada", status=404)

# mirror/views.py
from django.shortcuts import render, redirect

def home_redirect(request):
    """Redireciona para a página inicial do clone"""
    return render(request, 'index.html')

def admin_redirect(request):
    """Redireciona tentativas de acessar /admin"""
    return redirect('https://www.copart.com.br/admin')

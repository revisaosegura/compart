# mirror/views.py
from django.shortcuts import render, redirect

def home_redirect(request):
    """Redireciona para a página inicial do clone"""
    return redirect('/index.html')  # ou outro HTML espelhado


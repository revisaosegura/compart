import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def _serve_static_html(filename: str):
    """Serve an HTML file from the mirrored site directory."""
    base = os.path.join(settings.BASE_DIR, 'copart_clone', 'templates', 'copart')
    path = os.path.join(base, filename)
    if not os.path.exists(path):
        raise Http404
    with open(path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())


def home(request):
    return _serve_static_html('index.html')


def page(request, name):
    return _serve_static_html(f'{name}.html')


def cadastro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'cadastro.html', {'form': form})

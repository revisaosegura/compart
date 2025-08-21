import subprocess
import sys
import os
import re
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings
from .models import Cadastro
from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.core.mail import mail_admins


WHATSAPP_SNIPPET = (
    '<style>.wa-fab{position:fixed;right:20px;bottom:20px;z-index:9999;display:flex;'
    'align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;'
    'background:#25D366;box-shadow:0 6px 16px rgba(0,0,0,.2);}.wa-fab:hover{filter:brightness(0.95);}.'
    'wa-fab svg{width:28px;height:28px;fill:#fff;}</style>'
    '<a class="wa-fab" href="http://wa.me/5511958462009" target="_blank" rel="noopener">'
    '<svg viewBox="0 0 32 32"><path d="M16 .593C7.653.593.593 7.653.593 16c0 2.82.74 5.45 2.04 7.74L.593 32l8.41-1.97C11.28 31.26 13.58 32 16 32c8.347 0 15.407-7.06 15.407-15.407C31.407 7.653 24.347.593 16 .593zm0 28.48c-2.25 0-4.354-.63-6.146-1.72l-.44-.26-4.99 1.17 1.33-4.86-.29-.5C4.57 21.18 3.8 18.65 3.8 16 3.8 9.49 9.49 3.8 16 3.8c6.51 0 12.2 5.69 12.2 12.2 0 6.51-5.69 12.073-12.2 12.073zm7.04-8.74c-.39-.2-2.3-1.14-2.65-1.27-.36-.13-.62-.2-.88.2-.26.4-1 1.27-1.23 1.53-.23.26-.46.3-.85.1-.39-.2-1.64-.6-3.12-1.9-1.15-1.02-1.93-2.28-2.16-2.66-.23-.39-.02-.6.17-.79.18-.18.39-.46.59-.69.2-.23.26-.39.39-.65.13-.26.07-.5-.03-.69-.1-.2-.88-2.15-1.2-2.97-.31-.74-.63-.64-.88-.65-.23-.01-.5-.01-.77-.01-.27 0-.7.1-1.07.5-.36.4-1.4 1.37-1.4 3.34s1.43 3.88 1.63 4.15c.2.26 2.82 4.3 6.83 6.03.95.41 1.7.65 2.28.83.96.3 1.83.26 2.52.16.77-.11 2.3-.94 2.63-1.85.32-.92.32-1.72.23-1.89-.09-.17-.35-.27-.73-.45z"/></svg>'
    '</a>'
)


def _inject_whatsapp(html: str) -> str:
    return re.sub(r'</body\s*>', WHATSAPP_SNIPPET + '</body>', html, flags=re.IGNORECASE)

def _serve_static_html(filename: str):
    """Helper to return a static HTML file without template rendering."""
    base = os.path.join(settings.BASE_DIR, 'copart_clone', 'templates', 'copart')
    path = os.path.join(base, filename)
    if not os.path.exists(path):
        raise Http404
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = _inject_whatsapp(content)
    return HttpResponse(content)


def home(request):
    return _serve_static_html('index.html')

def page(request, name):
    # Corrige URLs duplicadas como /public/public/watchList
    match_public = re.match(r'^public/public/(.*)$', name)
    if match_public:
        return redirect('/public/' + match_public.group(1))
    if name == 'public/public':
        return redirect('/public/')

    # Mapeia URLs de lotes para arquivos estáticos
    lot_match = re.match(r'^lotSearchResults/lot/(\d+)(/Photos)?$', name)
    if lot_match:
        lot_id = lot_match.group(1)
        suffix = '_Photos' if lot_match.group(2) else ''
        filename = f'lot_{lot_id}{suffix}.html'
        return _serve_static_html(filename)

    return _serve_static_html(f'{name}.html')

def cadastro_view(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            cadastro = form.save()
            # Envia notificações para o admin
            message = f"Novo cadastro: {cadastro.nome} {cadastro.sobrenome}\nEmail: {cadastro.email}\nCPF/CNPJ: {cadastro.cpf_cnpj}"
            mail_admins('Novo cadastro', message)
            return redirect('sucesso')
    else:
        form = CadastroForm()
    response = render(request, "cadastro.html", {"form": form})
    response.content = _inject_whatsapp(response.content.decode("utf-8")).encode("utf-8")
    return response

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


def vehicle_alerts_overview(request):
    """Return placeholder page for /vehicleAlerts/overview."""
    return _serve_static_html('vehicleAlerts_overview.html')


def vehicle_alerts_mylots(request):
    """Return placeholder page for /vehicleAlerts/driverseat/mylots."""
    return _serve_static_html('vehicleAlerts_driverseat_mylots.html')

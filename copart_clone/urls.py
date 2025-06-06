from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView, RedirectView
from django.conf import settings

# Importa o módulo de views completo para evitar problemas de
# referência a funções individuais durante o carregamento.
from . import views

urlpatterns = [
    # Página inicial
    re_path(r'^favicon\.ico/?$', RedirectView.as_view(
        url=settings.STATIC_URL + 'images/favicon/copart/favicon.ico',
        permanent=True
    )),
    path('', views.home, name='home'),

    # URLs do app mirror
    path('mirror/', include('mirror.urls')),

    # Páginas estáticas comuns
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='about'),
    path('contato/', TemplateView.as_view(template_name='contato.html'), name='contact'),

    # Painel de administração
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('admin/copart_clone/agendar/<int:pk>/', views.agendar_scraper_view, name='copart_clone_agendar_scraper'),
    path('<str:name>/', views.page, name='page'),
]

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView, RedirectView
from django.conf import settings

# Importa o módulo de views completo para evitar problemas de
# referência a funções individuais durante o carregamento.
from core import views

urlpatterns = [
    # Página inicial
    re_path(r'^favicon\.ico/?$', RedirectView.as_view(
        url=settings.STATIC_URL + 'images/favicon/copart/favicon.ico',
        permanent=True
    )),
    path('', views.home, name='home'),
    path('index/', RedirectView.as_view(url='/', permanent=True)),

    # Painel de administração
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('<str:name>/', views.page, name='page'),
]

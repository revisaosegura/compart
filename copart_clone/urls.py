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
    path('index/', RedirectView.as_view(url='/', permanent=True)),

    # URLs do app mirror
    path('mirror/', include('mirror.urls')),

    # Páginas estáticas vindas do espelhamento
    path('login/', views.page, {'name': 'login'}, name='login'),
    path('sobre/', views.page, {'name': 'about'}, name='about'),
    path('contato/', views.page, {'name': 'contact'}, name='contact'),

    # Painel de administração
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('admin/copart_clone/agendar/<int:pk>/', views.agendar_scraper_view, name='copart_clone_agendar_scraper'),
    path('vehicleAlerts/overview', views.vehicle_alerts_overview, name='vehicle_alerts_overview'),
    path('vehicleAlerts/driverseat/mylots', views.vehicle_alerts_mylots, name='vehicle_alerts_mylots'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
    re_path(r'^(?P<name>.+)$', views.page, name='page'),
]

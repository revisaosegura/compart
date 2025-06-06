from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import cadastro_view, agendar_scraper_view, home, page

urlpatterns = [
    # Página inicial
    path('', home, name='home'),

    # URLs do app mirror
    path('mirror/', include('mirror.urls')),

    # Páginas estáticas comuns
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='about'),
    path('contato/', TemplateView.as_view(template_name='contato.html'), name='contact'),

    # Painel de administração
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('admin/copart_clone/agendar/<int:pk>/', agendar_scraper_view, name='copart_clone_agendar_scraper'),
    path('<str:name>/', page, name='page'),
]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from mirror import views

urlpatterns = [
    # Rota para a página inicial
    path('', views.home_redirect, name='home'),
    
    # Inclui as URLs do app mirror
    path('', include('mirror.urls')),
    
    # Rotas padrão para páginas comuns
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='about'),
    path('contato/', TemplateView.as_view(template_name='contato.html'), name='contact'),
    
    # Redirecionamento para áreas administrativas
    path('admin/', views.admin_redirect),
    path('painel/', views.admin_redirect),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Exemplo de rota adicional:
    # path('contato/', views.contato, name='contato'),
]

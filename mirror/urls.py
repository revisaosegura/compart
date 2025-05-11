# copart_clone/urls.py
from django.contrib import admin
from django.urls import path
from mirror import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('admin/', views.admin_redirect),
    # outras URLs do seu projeto...
]

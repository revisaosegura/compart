from django.contrib import admin
from django.urls import path, include
from .admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('vehicles.urls')),  # ✅ ESTA LINHA PRECISA EXISTIR
]

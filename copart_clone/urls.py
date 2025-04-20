from django.contrib import admin
from django.urls import path
from copart_clone import views  # ← Certifique-se que está importando corretamente

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),                # Página inicial
    path("executar-scraping/", views.run_scraper, name="scraping"),  # Executa scraping
]

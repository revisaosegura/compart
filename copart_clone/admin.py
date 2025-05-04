
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import FerramentasCopart
from .scraper import rodar_scraper  # Ajuste conforme o nome real do módulo

@admin.register(FerramentasCopart)
class FerramentasCopartAdmin(admin.ModelAdmin):
    change_list_template = "admin/index.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run/', self.admin_site.admin_view(self.run_scraper), name='run-scraper'),
        ]
        return custom_urls + urls

    def run_scraper(self, request):
        rodar_scraper()
        self.message_user(request, "Scraper executado com sucesso!", messages.SUCCESS)
        return HttpResponseRedirect("../")

from django.contrib import admin, messages
from django.urls import path
from django.http import HttpResponseRedirect
from .models import FerramentaCopart
from auto_scraper.scraper import start_scraping

@admin.register(FerramentaCopart)
class FerramentaCopartAdmin(admin.ModelAdmin):
    change_list_template = "admin/ferramentas_copart.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('atualizar-copart/', self.admin_site.admin_view(self.atualizar_copart), name='ferramenta_copart_run'),
        ]
        return custom_urls + urls

    def atualizar_copart(self, request):
        start_scraping()
        self.message_user(request, "✅ Scraping executado com sucesso.", level=messages.SUCCESS)
        return HttpResponseRedirect("../")

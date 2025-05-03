from django.contrib import admin, messages
from .models import FerramentaCopart
from auto_scraper.scraper import scrape_site

@admin.register(FerramentaCopart)
class FerramentaCopartAdmin(admin.ModelAdmin):
    change_list_template = "admin/ferramentas_copart.html"

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('atualizar-copart/', self.admin_site.admin_view(self.atualizar_copart), name='atualizar-copart')
        ]
        return custom_urls + urls

    def atualizar_copart(self, request):
        try:
            scrape_site()
            self.message_user(request, "✅ Site da Copart atualizado com sucesso!", messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"❌ Erro ao atualizar: {str(e)}", messages.ERROR)
        from django.shortcuts import redirect
        return redirect("..")
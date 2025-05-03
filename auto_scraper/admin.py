from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages
from .scraper import start_scraping  # importa a função que scrapeia

class FerramentasCopartAdmin(admin.ModelAdmin):
    change_list_template = "admin/ferramentas_copart.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('atualizar-copart/', self.admin_site.admin_view(self.atualizar_copart)),
        ]
        return my_urls + urls

    def atualizar_copart(self, request):
        try:
            start_scraping()  # chama a função de scrape
            self.message_user(request, "Atualização concluída com sucesso!", level=messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"Ocorreu um erro: {str(e)}", level=messages.ERROR)
        return HttpResponseRedirect("../")

admin.site.site_header = "Ferramentas Copart"
admin.site.index_title = "Área Administrativa"
admin.site.site_title = "Copart Admin"

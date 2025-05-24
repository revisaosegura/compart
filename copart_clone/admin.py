from django.contrib import admin, messages
from .models import Cadastro
from django.urls import path
from django.http import HttpResponseRedirect
import subprocess
from django.utils.html import format_html
from django.shortcuts import redirect
from .views import agendar_scraper_view

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'sobrenome', 'email', 'cpf_cnpj',
        'cidade', 'estado', 'telefone_celular', 'data_criacao'
    )
    change_list_template = "admin/copart_clone/cadastro_changelist.html"
   

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('executar-scraper/', self.admin_site.admin_view(self.executar_scraper), name='executar-scraper'),
        ]
        return custom_urls + urls

    def executar_scraper(self, request):
        try:
            subprocess.Popen(["python", "scraper.py"])
            self.message_user(request, "🚀 Scraper iniciado com sucesso!", messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"❌ Erro ao iniciar o scraper: {e}", messages.ERROR)
        return redirect("..")

import traceback
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class CustomAdminSite(admin.AdminSite):
    site_header = 'Ferramentas Copart'
    index_template = 'admin/custom_index.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-scraper/', self.admin_view(self.run_scraper), name='run-scraper'),
        ]
        return custom_urls + urls

    def run_scraper(self, request):
        try:
            print("🚀 Iniciando o scraper...")  # Log inicial
            rodar_scraper()  # Sua função real
            print("✅ Scraper finalizado sem erro.")
            self.message_user(request, "✅ Scraper executado com sucesso!", messages.SUCCESS)
        except Exception as e:
            tb = traceback.format_exc()
            print("❌ Erro ao rodar scraper:")
            print(tb)  # Isso vai mostrar TUDO no log da Render
            self.message_user(request, f"Erro ao rodar o scraper: {str(e)}", messages.ERROR)
        return redirect('/admin/')

admin_site = CustomAdminSite(name='customadmin')

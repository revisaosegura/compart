
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
        # Aqui você chama seu scraper real
        self.message_user(request, "Scraper executado com sucesso!", messages.SUCCESS)
        return HttpResponseRedirect(reverse('admin:index'))

admin_site = CustomAdminSite(name='customadmin')

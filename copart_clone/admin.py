
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html

from .models import ScraperPlaceholder  # Modelo simples para exibir o botão

class ScraperAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run-scraper/', self.admin_site.admin_view(self.run_scraper), name='run-scraper'),
        ]
        return custom_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['scraper_button'] = format_html(
            '<a class="button" href="{}">Rodar Scraper</a>',
            'run-scraper/'
        )
        return super().changelist_view(request, extra_context=extra_context)

    def run_scraper(self, request):
        # Aqui você chama sua função real do scraper
        # Exemplo: my_scraper_function()
        self.message_user(request, "Scraper executado com sucesso ✅", messages.SUCCESS)
        return redirect('..')

admin.site.register(ScraperPlaceholder, ScraperAdmin)

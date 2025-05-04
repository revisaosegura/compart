from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages
from .models import FerramentaCopart
from .tasks import executar_scraper  # Se você usa Celery ou outro método

@admin.register(FerramentaCopart)
class FerramentaCopartAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    change_list_template = "admin/index.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('run/', self.admin_site.admin_view(self.run_scraper), name='ferramenta_copart_run'),
        ]
        return custom_urls + urls

    def run_scraper(self, request):
        # Executa o scraper (ajuste para o seu método)
        executar_scraper()
        self.message_user(request, "🔄 Atualização iniciada com sucesso!", messages.SUCCESS)
        return redirect("..")

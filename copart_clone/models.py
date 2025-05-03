from django.db import models
from django.contrib import admin, messages
from django.contrib.auth.models import User
from auto_scraper.scraper import start_scraping


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions = ['atualizar_copart']

    def atualizar_copart(self, request, queryset):
        start_scraping()
        self.message_user(request, "✅ O scraping foi executado com sucesso.", level=messages.SUCCESS)

    atualizar_copart.short_description = "🔄 Atualizar Copart Agora"

class FerramentaCopart(models.Model):
    nome = models.CharField(max_length=255, default="Ferramenta Copart", editable=False)

    def __str__(self):
        return "Ferramenta Copart"

    class Meta:
        verbose_name = "Ferramenta Copart"
        verbose_name_plural = "Ferramentas Copart"

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages
from auto_scraper.scraper import start_scraping

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions = ['atualizar_copart']

    def atualizar_copart(self, request, queryset):
        start_scraping()
        self.message_user(request, "✅ O scraping foi executado com sucesso.", level=messages.SUCCESS)

    atualizar_copart.short_description = "🔄 Atualizar Copart Agora"
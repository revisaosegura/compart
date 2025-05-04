
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import AtualizarTemplates

class AtualizarTemplatesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        if 'executar' in request.GET:
            # 🔥 Aqui você coloca sua função para rodar o scraper real
            # from .scraper import rodar_scraper
            # rodar_scraper()
            messages.success(request, "✅ Scraper executado com sucesso!")
            return HttpResponseRedirect(request.path)
        return super().changelist_view(request, extra_context)

admin.site.register(AtualizarTemplates, AtualizarTemplatesAdmin)

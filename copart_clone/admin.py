from django.contrib import admin, messages
from .admin_tools import FerramentasCopartAdmin
from .models import FerramentaCopart
from auto_scraper.scraper import start_scraping

@admin.register(FerramentaCopart)
class FerramentaCopartAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if 'run' in request.GET:
            start_scraping()
            self.message_user(request, "✅ Scraping executado com sucesso.", level=messages.SUCCESS)
        return super().changelist_view(request, extra_context)

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('run/', self.admin_site.admin_view(self.changelist_view), name='ferramenta_copart_run'),
        ]
        return custom_urls + urls
    
@admin.register(object)
class DummyAdmin(FerramentasCopartAdmin):
    pass

@admin.register(FerramentaCopart)
class FerramentaCopartAdminView(FerramentasCopartAdmin):
    pass

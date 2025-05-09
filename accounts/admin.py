from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'cpf', 'rg')
    search_fields = ('full_name', 'email', 'cpf', 'rg')
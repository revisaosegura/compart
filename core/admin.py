from django.contrib import admin
from .models import UserRegistration


@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone', 'cpf', 'criado_em')

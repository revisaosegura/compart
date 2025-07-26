from django import forms
from .models import UserRegistration


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = [
            'nome_completo',
            'email',
            'telefone',
            'cpf',
        ]

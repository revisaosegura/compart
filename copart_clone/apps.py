from django.apps import AppConfig
from django.contrib.auth import get_user_model


class CopartCloneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'copart_clone'

    def ready(self):
        User = get_user_model()
        username = 'copart2025'
        password = 'Copart.2025'
        email = 'admin@example.com'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)

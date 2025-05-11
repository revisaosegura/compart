import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'copart_clone.settings')

# Configuração base da aplicação
application = get_wsgi_application()

# Adiciona WhiteNoise para servir arquivos estáticos
application = WhiteNoise(
    application,
    root=os.path.join(os.path.dirname(__file__), 'staticfiles'),
    prefix='/static/',
)

# Adiciona suporte para arquivos estáticos adicionais
application.add_files(
    os.path.join(os.path.dirname(__file__), 'mirror/static'),
    prefix='/mirror-static/'
)
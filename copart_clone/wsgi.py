import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'copart_clone.settings')

application = get_wsgi_application()

# Corrigido para apontar corretamente para a pasta 'static'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

application = WhiteNoise(application, root=STATIC_ROOT, prefix='/static/')

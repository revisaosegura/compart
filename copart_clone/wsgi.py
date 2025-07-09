import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'copart_clone.settings')

application = get_wsgi_application()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Serve arquivos estaticos coletados
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

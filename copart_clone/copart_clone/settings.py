import os
from pathlib import Path
import environ

# Inicializa environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = env('SECRET_KEY', default='django-insecure-+fake-key-for-dev-only@')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Para desenvolvimento
    'mirror.apps.MirrorConfig',  # Forma mais explícita de registrar o app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mirror.middleware.MirrorMiddleware',  # Middleware personalizado
]

ROOT_URLCONF = 'copart_clone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretório global de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
            ],
            'builtins': [],  # Adicione aqui qualquer template tag library global
        },
    },
]

WSGI_APPLICATION = 'copart_clone.wsgi.application'

# Database (opcional - caso precise no futuro)
# DATABASES = {
#     'default': env.db(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')),
# }

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mirror/static'),
    os.path.join(BASE_DIR, 'static'),  # Diretório global de static files
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WhiteNoise configuration
WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0  # 1 year cache in production
WHITENOISE_USE_FINDERS = DEBUG

# Security settings
if not DEBUG:
    # HTTPS settings
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # Security headers
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'DENY'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Custom settings (opcional - para configurações específicas do projeto)
MIRROR_CONFIG = {
    'CACHE_TIMEOUT': env.int('MIRROR_CACHE_TIMEOUT', default=3600),  # 1 hora
    'USER_AGENT': env('MIRROR_USER_AGENT', default='Mozilla/5.0'),
}

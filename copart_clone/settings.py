import os
from pathlib import Path
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = env('SECRET_KEY', default='your-secret-key-here')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = ['copart-clone.onrender.com', 'localhost', '127.0.0.1', 'copartbr.com.br', 'www.copartbr.com.br']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',              # ✅ necessário para o Django Admin
    'django.contrib.auth',              # ✅ necessário para autenticação
    'django.contrib.contenttypes',      # ✅ necessário para models genéricos
    'django.contrib.sessions',          # ✅ necessário para sessões
    'django.contrib.messages',          # ✅ necessário para mensagens
    'django.contrib.staticfiles',       # ✅ necessário para arquivos estáticos
    'whitenoise.runserver_nostatic',
    'core.apps.CoreConfig',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ✅ necessário
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',             # ✅ necessário para formulários admin
    'django.contrib.auth.middleware.AuthenticationMiddleware', # ✅ necessário
    'django.contrib.messages.middleware.MessageMiddleware',  # ✅ necessário
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ClonedSiteMiddleware',
]

ROOT_URLCONF = 'copart_clone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'copart_clone/templates/copart'],  # ou [] se não tiver pasta de templates personalizada
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',         # ✅ Necessário
                'django.contrib.messages.context_processors.messages', # ✅ Necessário
            ],
        },
    },
]

WSGI_APPLICATION = 'copart_clone.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'copart_clone', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# Whitenoise
WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0
WHITENOISE_USE_FINDERS = DEBUG
WHITENOISE_AUTOREFRESH = DEBUG

# Project-specific settings
MIRROR_SETTINGS = {
    'BASE_URL': 'https://www.copart.com.br',
    'CACHE_EXPIRY': env.int('CACHE_EXPIRY', default=3600),  # 1 hour
}

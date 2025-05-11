#!/bin/bash
set -o errexit

# Configura o ambiente para o Playwright
export PLAYWRIGHT_BROWSERS_PATH=/opt/render/.cache/ms-playwright

# Instala dependências Python
pip install -r requirements.txt

# Instala os browsers
python scraper.py --install-only

# Executa o scraper principal
python scraper.py

# Prepara arquivos estáticos
python manage.py collectstatic --noinput
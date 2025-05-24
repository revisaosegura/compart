#!/bin/bash
set -o errexit

# Configura caminhos absolutos
PROJECT_DIR="/opt/render/project/src"
cd $PROJECT_DIR

# Instala dependências
pip install -r requirements.txt

# Instala Playwright
export PLAYWRIGHT_BROWSERS_PATH=$PROJECT_DIR/.playwright
python -m playwright install
python -m playwright install-deps
playwright install --with-deps

# Executa o scraper
python scraper.py

# Coleta arquivos estáticos
python manage.py collectstatic --noinput
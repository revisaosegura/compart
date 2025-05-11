#!/bin/bash
set -o errexit

# Configuração específica para o Render
export PLAYWRIGHT_BROWSERS_PATH=0  # Usa browsers bundlados

# Instala dependências Python
pip install -r requirements.txt

# Instala browsers do Playwright (modo bundlado)
python -c "from playwright.__main__ import main; main(['install'])"

# Roda o scraper
python scraper.py

# Prepara arquivos estáticos
python manage.py collectstatic --noinput
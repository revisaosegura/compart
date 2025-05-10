#!/bin/bash
set -o errexit

# Instala dependências do sistema para o Playwright
apt-get update
apt-get install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2

# Instala dependências Python
pip install -r requirements.txt

# Instala browsers do Playwright
playwright install-deps
playwright install

# Roda o scraper
python scraper.py

# Prepara os arquivos estáticos
python manage.py collectstatic --noinput
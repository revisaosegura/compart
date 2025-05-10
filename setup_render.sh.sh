#!/bin/bash

# Instala dependências
pip install -r requirements.txt

# Configura o Playwright
playwright install
playwright install-deps

# Executa o scraper
python scraper.py

# Configuração do Django
python manage.py migrate
python manage.py collectstatic --noinput
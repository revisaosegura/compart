#!/bin/bash

# Instala dependências
pip install -r requirements.txt

# Configura o Playwright
playwright install
playwright install-deps
playwright install --with-deps

# O scraper demanda muita memória e deve ser executado apenas sob demanda.

# Configuração do Django
python manage.py migrate
python manage.py collectstatic --noinput

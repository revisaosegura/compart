#!/usr/bin/env bash
# Instala dependências
pip install -r requirements.txt
# Roda collectstatic para o admin ficar bonito
python manage.py collectstatic --no-input

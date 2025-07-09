#!/bin/bash
# Instala dependências e prepara o ambiente para execução local no Codex.
#
# Atenção: este script precisa de acesso à internet para baixar pacotes.
# Caso sua sessão Codex esteja sem rede, forneça os arquivos *.whl
# manualmente ou ajuste este script para usar um mirror interno.

set -o errexit

# Instala pacotes Python
pip install -r requirements.txt

# Instala e configura Playwright
export PLAYWRIGHT_BROWSERS_PATH=$(pwd)/.playwright
python -m playwright install
python -m playwright install-deps
playwright install --with-deps

# Roda o scraper para baixar o site antes dos testes
python scraper.py || true

# Prepara o Django
python manage.py migrate
python manage.py collectstatic --noinput

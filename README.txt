PASSOS NO WINDOWS:

1. Crie o ambiente virtual:
python -m venv venv
venv\Scripts\activate

2. Instale dependências:
pip install -r requirements.txt
playwright install

3. Rode o scraper:
python scraper.py

4. Rode o Django:
python manage.py migrate
python manage.py runserver

5. Acesse no navegador:
http://127.0.0.1:8000/

6. Para hospedar de forma gratuita na Render:
   - Conecte este repositório em um novo Web Service.
   - A plataforma irá executar o `render.yaml`, instalar dependências, rodar o scraper e iniciar o Django automaticamente.

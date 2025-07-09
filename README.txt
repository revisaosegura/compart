PASSOS NO WINDOWS:

1. Crie o ambiente virtual:
python -m venv venv
venv\Scripts\activate

2. Instale dependências:
pip install -r requirements.txt
playwright install

Em sessões Codex ou ambientes sem dependências pré-instaladas,
execute `bash setup_codex.sh` para baixar e configurar tudo de uma vez.

3. Rode o scraper **antes de iniciar o Django** (execute novamente sempre que quiser atualizar as páginas espelhadas):
python scraper.py

4. Rode o Django:
python manage.py migrate
python manage.py runserver

5. Acesse no navegador:
http://127.0.0.1:8000/

6. Para hospedar de forma gratuita na Render:
   - Conecte este repositório em um novo Web Service.
   - A cada **Deploy latest commit**, o Render executará `build.sh` (conforme `render.yaml`).
     Esse script instala dependências, roda o scraper e coleta arquivos estáticos
     antes de iniciar o Django automaticamente.

7. **Resolvido conflitos de merge:**
   - Caso o GitHub indique conflitos ao criar o pull request, clique em "Resolve conflicts".
   - Edite o arquivo para manter apenas o conteúdo desejado, removendo os marcadores `<<<<<<<`, `=======` e `>>>>>>>`.
   - Após salvar, conclua o merge commit diretamente pela interface web.

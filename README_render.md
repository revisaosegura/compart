# Deploy no Render

Este projeto está pronto para funcionar como espelho do site https://www.copart.com.br/ no Render.

## Passos para Deploy:

1️⃣ Suba para o GitHub normalmente:
```bash
git add .
git commit -m "Projeto corrigido e pronto para Render"
git push origin main
```

2️⃣ No Render:
- Crie um novo serviço Web Service;
- Conecte com seu repositório;
- Configure:
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `gunicorn copart_clone.wsgi`
    - **Environment:** Python 3.x
    - **Disk:** (mantém SQLite ou recomenda Postgres para produção)

3️⃣ No Admin (/admin):
- Use o botão **"Atualizar Copart"** para rodar o scraper.

✅ Pronto!
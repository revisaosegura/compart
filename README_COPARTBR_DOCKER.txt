# CopartBR Mirror (Nginx + Docker)

## Estrutura esperada do build
Antes de criar a imagem, **rode o scraper** para gerar a pasta `copart_clone/` com esta estrutura:

```
copart_clone/
├─ static/
│  └─ copart/
│     ├─ api/                 # JSONs capturados + api_manifest.json
│     ├─ css, js, img, etc.
└─ templates/
   └─ copart/
      ├─ index.html
      ├─ ...demais páginas espelhadas...
```

## Build
```
docker build -t copartbr-mirror:latest .
```

## Run
```
docker run --rm -p 8080:80 \
  --name copartbr \
  copartbr-mirror:latest
```
Abra: http://localhost:8080

## Produção (domínio)
Aponte `A`/`CNAME` para o host que rodará o container e publique a porta 80/443.
Para HTTPS, coloque um proxy (Caddy/Traefik/Nginx na borda) ou monte certificados no container.

## Observações
- O botão do WhatsApp está no HTML espelhado; para apontar para seu link final, rode o scraper com `WHATSAPP_NUMBER` ou edite o atributo `href` (procurar `.wa-fab`).
- As chamadas dinâmicas de API podem ser atendidas pelos JSONs locais (`/static/copart/api/...`) via wrapper JS do scraper; quando não houver no manifest, o Nginx acima faz **fallback** para o domínio original.
- Se quiser bloquear por completo o fallback ao domínio original, remova o bloco `location ~ ^/(services|api|...)`.

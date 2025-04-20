import os
import shutil
from pathlib import Path

ORIGEM = Path("copart_site")
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

# Cria diretórios se não existirem
TEMPLATES_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)

# Extensões de arquivos estáticos
EXT_STATIC = (".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".woff", ".ttf", ".otf")

print("🚚 Movendo arquivos para o Django...")

for root, dirs, files in os.walk(ORIGEM):
    for file in files:
        caminho_antigo = Path(root) / file
        rel_path = caminho_antigo.relative_to(ORIGEM)

        if file.endswith(".html"):
            destino = TEMPLATES_DIR / rel_path
        elif file.endswith(EXT_STATIC):
            destino = STATIC_DIR / rel_path
        else:
            continue  # Ignora outros arquivos

        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(caminho_antigo, destino)
        print(f"✅ Copiado: {rel_path} → {'templates/' if file.endswith('.html') else 'static/'}")

print("\n🎉 Tudo pronto! Agora configure suas rotas e views no Django para usar esses templates.")

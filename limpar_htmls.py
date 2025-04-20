import os
import re

CAMINHO_PASTA = "copart_site"

# Padrões que indicam scripts desnecessários ou links externos
PADROES_REMOVER = [
    r'<script[^>]*src="[^"]*(incapsula|akamai|cloudfront|datadome)[^"]*"[^>]*></script>',
    r'<link[^>]*href="[^"]*(incapsula|akamai|cloudfront|datadome)[^"]*"[^>]*>',
    r'<img[^>]*src="[^"]*(incapsula|akamai|cloudfront|datadome)[^"]*"[^>]*>',
    r'<script[^>]*>[^<]*(Incapsula|akamai|datadome)[^<]*</script>',
    r'<script[^>]*src=".*\.js.*"[^>]*></script>',
    r'<script>.*?(Incapsula|akamai|datadome|Cloudfront).*?</script>',
]

def limpar_html(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    for padrao in PADROES_REMOVER:
        conteudo = re.sub(padrao, "", conteudo, flags=re.IGNORECASE | re.DOTALL)

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

def processar_pasta(caminho):
    for raiz, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo.endswith(".html"):
                caminho_completo = os.path.join(raiz, arquivo)
                print(f"🧹 Limpando {caminho_completo}")
                limpar_html(caminho_completo)

if __name__ == "__main__":
    processar_pasta(CAMINHO_PASTA)
    print("✅ Limpeza concluída!")

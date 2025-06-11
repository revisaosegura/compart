import os
import re
import time
import urllib.parse
from collections import deque
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from typing import Set

BASE_URL = "https://www.copart.com.br"
START_PAGES = [
    "/",  # página inicial
    "/how-it-works/",  # guia de funcionamento
    "/sellForIndividuals/",  # venda de veículos
    "/doRegistration",  # cadastro
    "/login/",  # página de login
]

TEMPLATE_DIR = os.path.join("copart_clone", "templates", "copart")
STATIC_DIR = os.path.join("copart_clone", "static", "copart")

# Mapeia URL de origem para o nome do arquivo HTML local
URL_TO_SLUG = {}

def normalizar_caminho(url_path: str) -> str:
    """Remove query strings e fragmentos."""
    parsed = urllib.parse.urlparse(url_path)
    path = parsed.path
    if not path.startswith("/"):
        path = "/" + path
    return path.rstrip("/") or "/"

def sanitize_filename(url_path: str) -> str:
    """Sanitiza caminhos de arquivo mantendo a estrutura de pastas."""
    path = url_path.split("?")[0].split("#")[0].lstrip("/")
    parts = [re.sub(r'[<>:"/\\|?*]', '_', p) for p in path.split("/") if p]
    if not parts:
        return "index"
    return os.path.join(*parts)

def baixar_arquivo(url: str, destino: str) -> None:
    """Faz download de um arquivo respeitando a estrutura de pastas."""
    if "Incapsula" in url or "nly-Fathere" in url:
        return
    if os.path.exists(destino):
        return
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as f:
                f.write(response.content)
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")


def baixar_recursos_css(css_path: str, origem_url: str) -> None:
    """Baixa recursos referenciados dentro de um CSS."""
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except Exception:
        return

    def substituir(match: re.Match) -> str:
        recurso = match.group(1).strip('"\' ')
        if recurso.startswith("data:") or recurso.startswith("http"):
            return match.group(0)
        full = urllib.parse.urljoin(origem_url, recurso)
        sanitized = sanitize_filename(recurso)
        local = os.path.join(STATIC_DIR, sanitized)
        baixar_arquivo(full, local)
        return f"url('/static/copart/{sanitized}')"

    novo_conteudo = re.sub(r"url\(([^)]+)\)", substituir, conteudo)
    if novo_conteudo != conteudo:
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(novo_conteudo)


def proteger_template(html):
    html = re.sub(r"{{(.*?)}}", r"{% raw %}{{\1}}{% endraw %}", html)
    return html


def coletar_links(soup) -> Set[str]:

    """Retorna todos os links internos encontrados na página."""
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("javascript:") or href.startswith("mailto:"):
            continue
        if href.startswith("http"):
            if not href.startswith(BASE_URL):
                continue
            path = urllib.parse.urlparse(href).path
        else:
            path = href
        normalized = normalizar_caminho(path)
        links.add(normalized)
    return links

def processar_pagina(page, url_path):
    """Baixa uma página e retorna novos links encontrados."""
    slug = URL_TO_SLUG.setdefault(url_path, sanitize_filename(url_path))

    page.goto(BASE_URL + url_path, timeout=60000, wait_until="networkidle")
    page.wait_for_load_state("networkidle")
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    base_tag = soup.find("base")
    if base_tag:
        base_tag["href"] = "/"
    elif soup.head:
        soup.head.insert(0, soup.new_tag("base", href="/"))

    # baixar e corrigir assets
    for tag in soup.find_all(["script", "link", "img"]):
        attr = "src" if tag.name != "link" else "href"
        url = tag.get(attr)
        if not url:
            continue
        if url.startswith("http") or url.startswith("data"):
            continue
        if "Incapsula" in url or "nly-Fathere" in url:
            tag.decompose()
            continue
        full_url = urllib.parse.urljoin(BASE_URL, url)
        sanitized = sanitize_filename(url)
        local_path = os.path.join(STATIC_DIR, sanitized)
        baixar_arquivo(full_url, local_path)
        if local_path.endswith('.css'):
            baixar_recursos_css(local_path, full_url)
        tag[attr] = f"/static/copart/{sanitized}"

    links = coletar_links(soup)

    html_final = proteger_template(str(soup))

    # salvar HTML
    html_path = os.path.join(TEMPLATE_DIR, f"{slug}.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"[✓] Página salva: {url_path} → {html_path}")

    return links

    
def salvar_site():
    os.makedirs(STATIC_DIR, exist_ok=True)
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    fila = deque(normalizar_caminho(p) for p in START_PAGES)
    visitados = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        while fila:
            url_path = fila.popleft()
            if url_path in visitados:
                continue
            try:
                novos_links = processar_pagina(page, url_path)
                visitados.add(url_path)
                for link in novos_links:
                    if link not in visitados:
                        fila.append(link)
            except Exception as e:
                print(f"[!] Erro na página {url_path}: {e}")
        browser.close()


if __name__ == "__main__":
    salvar_site()

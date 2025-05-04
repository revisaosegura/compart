import os
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from undetected_chromedriver import Chrome, ChromeOptions
from django.core.management.base import BaseCommand

URL = "https://www.copart.com.br/"
TEMPLATE_PATH = "copart_clone/templates/copart/index.html"

def proteger_variaveis(html):
    html = re.sub(r"({{.*?}})", r"{% raw %}\\1{% endraw %}", html)
    html = re.sub(r"(::locale\\.messages\\[.*?\\])", r"{% raw %}\\1{% endraw %}", html)
    return html

class Command(BaseCommand):
    help = "Atualiza o index.html da Copart espelho, quebrando o Incapsula"

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Iniciando download da página da Copart com Selenium...")

        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")

        try:
            driver = Chrome(options=chrome_options)
            driver.get(URL)
            time.sleep(5)  # Aguarda a página carregar completamente

            html = driver.page_source
            html = proteger_variaveis(html)

            os.makedirs(os.path.dirname(TEMPLATE_PATH), exist_ok=True)

            with open(TEMPLATE_PATH, "w", encoding="utf-8") as f:
                f.write(html)

            self.stdout.write(self.style.SUCCESS(f"✅ index.html atualizado e salvo em {TEMPLATE_PATH}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Erro: {e}"))
        finally:
            driver.quit()
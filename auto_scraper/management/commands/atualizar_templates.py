from django.core.management.base import BaseCommand
from auto_scraper.scraper import start_scraping
import os
import shutil


def limpar_templates_antigos():
    pasta_templates = os.path.join("templates", "copart")
    if os.path.exists(pasta_templates):
        for root, dirs, files in os.walk(pasta_templates):
            for file in files:
                if file.endswith(".html"):
                    caminho_arquivo = os.path.join(root, file)
                    os.remove(caminho_arquivo)
        print("🧹 Templates antigos removidos.")
    else:
        print("⚠️ Pasta de templates ainda não existe. Nada para limpar.")


class Command(BaseCommand):
    help = "Atualiza os templates com os dados mais recentes do site Copart."

    def handle(self, *args, **kwargs):
        print("🚀 Iniciando atualização dos templates...")
        scraper.start_scraping()
        scraper.limpar_templates_antigos("copart_clone/templates/copart")
        print("✅ Templates atualizados com sucesso.")

from django.core.management.base import BaseCommand
from auto_scraper import scraper

class Command(BaseCommand):
    help = "Atualiza os templates copiando novamente do site original e protegendo expressões Django"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🚀 Iniciando atualização dos templates..."))

        # Remove templates antigos antes de iniciar o scraping
        self.stdout.write("🧹 Removendo templates antigos...")
        scraper.limpar_templates_antigos()

        # Inicia o processo de scraping
        self.stdout.write("📡 Iniciando cópia dos templates com Selenium...")
        scraper.start_scraping()

        self.stdout.write(self.style.SUCCESS("✅ Templates atualizados com sucesso."))

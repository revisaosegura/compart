from django.core.management.base import BaseCommand
from auto_scraper import scraper

class Command(BaseCommand):
    help = "Atualiza os templates copiando novamente do site original"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🚀 Iniciando atualização dos templates..."))
        scraper.start_scraping()
        self.stdout.write(self.style.SUCCESS("✅ Templates atualizados com sucesso."))
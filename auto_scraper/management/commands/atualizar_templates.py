from django.core.management.base import BaseCommand
from auto_scraper.scraper import start_scraping  # certifique-se que esse import está correto

class Command(BaseCommand):
    help = 'Executa o scraping da Copart e atualiza os templates HTML.'

    def handle(self, *args, **kwargs):
        self.stdout.write('🚀 Iniciando atualização dos templates...')
        start_scraping()
        self.stdout.write(self.style.SUCCESS('✅ Templates atualizados com sucesso.'))


from django.db import models

class ScraperPlaceholder(models.Model):
    name = models.CharField(max_length=100, default="Executar Scraper")

    class Meta:
        verbose_name = "Executar Scraper"
        verbose_name_plural = "Executar Scraper"

    def __str__(self):
        return self.name

class FerramentaScraper(models.Model):
    class Meta:
        verbose_name = 'Atualizar Templates'
        verbose_name_plural = 'Ferramenta: Atualizar Templates'
        managed = False  # NÃO cria tabela

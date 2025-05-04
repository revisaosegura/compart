
from django.db import models

class ScraperPlaceholder(models.Model):
    name = models.CharField(max_length=100, default="Executar Scraper")

    class Meta:
        verbose_name = "Executar Scraper"
        verbose_name_plural = "Executar Scraper"

    def __str__(self):
        return self.name

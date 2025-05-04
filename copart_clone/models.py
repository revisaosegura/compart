
from django.db import models

class AtualizarTemplates(models.Model):
    class Meta:
        verbose_name = 'Executar Atualização'
        verbose_name_plural = '⚙️ Atualizar Templates (Executar Scraper)'
        managed = False  # ✅ NÃO cria tabela no banco

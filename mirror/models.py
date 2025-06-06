# mirror/models.py
from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

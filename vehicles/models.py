from django.db import models

class Vehicle(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    image = models.ImageField(upload_to='vehicles/')
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    bid = models.CharField(max_length=100)
    origin_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

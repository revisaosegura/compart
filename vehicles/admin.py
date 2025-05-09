from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'model', 'year', 'is_sold', 'location')
    search_fields = ('title', 'brand', 'model', 'year')
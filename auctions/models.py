from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle

class Auction(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    end_time = models.DateTimeField()
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Auction: {self.vehicle.title}"

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"

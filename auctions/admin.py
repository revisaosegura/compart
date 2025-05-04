from django.contrib import admin
from .models import Auction, Bid

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'end_time', 'current_bid')
    search_fields = ('vehicle__title',)

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('auction', 'user', 'amount', 'timestamp')
    search_fields = ('auction__vehicle__title', 'user__username')
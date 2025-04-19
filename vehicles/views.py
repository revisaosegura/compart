from django.shortcuts import render, get_object_or_404, redirect
from vehicles.models import Vehicle
from auctions.models import Auction, Bid
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    auction = Auction.objects.filter(vehicle=vehicle).first()
    bids = Bid.objects.filter(auction=auction).order_by('-timestamp') if auction else []

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/admin/login/?next=' + request.path)  # ou crie tela de login
        bid_value = request.POST.get('bid_value')
        if auction and bid_value:
            Bid.objects.create(
                auction=auction,
                user=request.user,
                amount=bid_value,
            )
            auction.current_bid = bid_value
            auction.save()
            return redirect('vehicle_detail', vehicle_id=vehicle_id)

    context = {
        'vehicle': vehicle,
        'auction': auction,
        'bids': bids
    }
    return render(request, 'vehicles/detail.html', context)

def vehicle_list(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    return render(request, 'vehicles/list.html', {'vehicles': vehicles})

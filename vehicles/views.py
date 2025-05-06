from django.shortcuts import render

# View principal
def home(request):
    return render(request, "copart/index.html")

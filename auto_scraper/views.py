# copart_clone/views.py
from django.shortcuts import render
from auto_scraper.scraper import start_scraping

def home(request):
    return render(request, "copart/index.html")

def run_scraper(request):
    start_scraping()
    return render(request, "copart/index.html")

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<h1>I am energetic today</h1>")
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def prodView(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    return render(request, 'shop/checkout')

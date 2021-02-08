from django.shortcuts import render
from frontend.models import *

# Create your views here.

def index(request):
    profile =Sponsored.objects.all()
    profile2 =Latest.objects.all()
    profile3 =Featured.objects.all()
    images = {'spon':profile, 'lat':profile2, 'fat':profile3}
    return render(request, 'frontend/index.html', images)

def buy(request):
    return render(request, 'frontend/buy.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def properties(request):
    return render(request, 'frontend/properties.html')

def rent(request):
    return render(request, 'frontend/rent.html')

def login(request):
    return render(request, 'frontend/login.html')

def signup(request):
    return render(request, 'frontend/signup.html')
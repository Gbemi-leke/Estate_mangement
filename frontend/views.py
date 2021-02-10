from django.shortcuts import render
from frontend.models import *

# Create your views here.

def index(request):
    profile =Property.objects.all()[:4]
    featured=Property.objects.all().filter(featured=True)[:4]
    sponsored=Property.objects.all().filter(sponsored=True)[:4]
    
    profile2 =Agents.objects.all()
    photos = {'pro':profile,'featured':featured, 'sponsored':sponsored, 'agent':profile2 }
    return render(request, 'frontend/index.html', photos)

def buy(request):
    sale = Buy.objects.all()[:6]
    return render(request, 'frontend/buy.html', {'buy':sale})

def contact(request):
    return render(request, 'frontend/contact.html')

def rent(request):
    hire = Rent.objects.all()[:6]
    return render(request, 'frontend/rent.html', {'rent':hire})

def login(request):
    return render(request, 'frontend/login.html')

def signup(request):
    return render(request, 'frontend/signup.html')
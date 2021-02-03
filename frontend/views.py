from django.shortcuts import render
from frontend.models import Biography

# Create your views here.

def index(request):
    profile = Biography.objects.all()
    return render(request, 'frontend/index.html', {'bio':profile})

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
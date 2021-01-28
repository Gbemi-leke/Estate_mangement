from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

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
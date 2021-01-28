from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.buy, name='buy'),
    path('contact-page', views.contact, name='contact'),
    path('properties-page', views.properties, name='properties'),
    path('rent-page', views.rent, name='rent'),
    path('login-page', views.login, name='login'),
    path('signup-page', views.signup, name='signup'),
]
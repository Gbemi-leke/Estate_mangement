from django.urls import path
from django.conf.urls import url 
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.buy, name='buy'),
    path('contact-page', views.contact, name='contact'),
    path('rent-page', views.rent, name='rent'),
    path('login-page', views.login, name='login'),
    path('signup-page', views.signup, name='signup'),
]
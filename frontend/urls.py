from django.urls import path
from django.conf.urls import url 
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.buy, name='buy'),
    path('detail/<int:buy_id>/', views.detail_buy, name='detail_buy'),
    path('contact-page', views.contact, name='contact'),
    path('contact2/<int:agent_id>/', views.contact2, name='contact2'),
    path('filter-data/', views.filter_data, name='filter_data'),
    path('rent-page', views.rent, name='rent'),
    path('details/<int:rent_id>/', views.detail_rent, name='detail_rent'),
    path('signup-page', views.signup, name='signup'),
    path('user-page', views.user, name='user'),
]
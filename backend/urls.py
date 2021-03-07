from django.urls import path
from django.conf.urls import url 
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout_view-page/', views.logout_view, name='logout_view'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('user_profile-page/', views.user_profile, name='user_profile'),
    path('edit_form-page/', views.edit_form, name='edit_form'),
    path('edit_newform-page/', views.edit_newform, name='edit_newform'),
    path('pass_form-page/', views.pass_form, name='pass_form'),
    path('reset/', views.reset, name='reset'),
    path('admin-login-page/', views.login_userview, name='login_userview'),
    path('messages-page/', views.messages, name='messages'),
    path('success-message/', views.success_message, name='success_message'),
    path('register-page/', views.register_form, name='register_form'),
    path('logout/', views.logout_view, name='logout_view'),
    path('listings2-page/', views.listings, name='listings'),
    path('listings-page/', views.view_listing, name='view_listing'),
    path('add-newlisting-page/', views.add_newlisting, name='add_newlisting'),
    path('admin-newlisting-page/', views.admin_newlisting, name='admin_newlisting'),
    path('listings-page/', views.new_listings, name='new_listings'),
   
]
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.views.generic import ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView 

from django.contrib import messages

from frontend.models import *
from backend.forms import *

# Create your views here.


@login_required(login_url='/dashboard_page/')
def dashboard(request):
    if request.user.is_staff:
        return render(request, 'backend/index.html')
    else: 
        return render(request, 'backend/user.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # if request.user.is_staff:
        #     return render(request, 'backend/admin.html')
        # else: 
        #     return render(request, 'backend/index.html')

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username and Password do not match')
        
    return render(request, 'frontend/login2.html')

def login_userview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/userlogin.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def success_message(request):
    return render(request, 'backend/success.html')

def add_newlisting(request):
    if request.method == 'POST':
        list_form = ListingForm(request.POST, request.FILES)
        if list_form.is_valid():
            listf = list_form.save(commit=False)
            listf.user = request.user
            listf.save()
            # messages.success(request, 'Hotel Posted')
            
    else:
        list_form = ListingForm()
    return render(request, 'backend/add-newlisting.html', {'listf': list_form})

def edit_newlisting(request, post_id):
    single_post = get_object_or_404(AddProperty, id=post_id)
    if request.method == 'POST':
        post_form = ListingForm(request.POST, request.FILES, instance=single_post)
        if post_form.is_valid():
            listf = post_form.save(commit=False)
            listf.user = request.user
            listf.save()
            # messages.success(request, 'Hotel Posted')
            
    else:
        post_form = ListingForm(instance=single_post)
    return render(request, 'backend/edit_post.html', {'editf': post_form})

def view_listing(request):
    property_list = AddProperty.objects.filter(user=request.user)
    return render(request, 'backend/listings.html', {'hlist':property_list})

def new_listings(request):
    hotel_list = AddProperty.objects.filter(user=request.user)
    return render(request, 'backend/newlistings.html', {'hlist':hotel_list})

def view_newlistingdetails(request, pk):
    post = get_object_or_404(AddProperty, pk=pk)
    return render(request, 'backend/view-newlisting.html', {'pst':post})

def delete_newproperty(request, listf_id):
    post_record = get_object_or_404(AddProperty, id=listf_id)
    post_record.delete()
    return redirect('backend:new_listings')

def register_form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # messages.success(request, 'Succesfully Registered')
            return redirect('backend:success_message')
    else:
        register_form = RegisterForm() 
    return render(request, 'frontend/signup.html', {'reg': register_form})


def add_newlisting(request):
    if request.method == 'POST':
        list_form = ListingForm(request.POST, request.FILES)
        if list_form.is_valid():
            listf = list_form.save(commit=False)
            listf.user = request.user
            listf.save()
            # messages.success(request, 'Hotel Posted')
    else:
        list_form = ListingForm()
    return render(request, 'backend/add-newlisting.html', {'listf': list_form})
@login_required(login_url='/dashboard/')
def messages(request):
    return render(request, 'backend/messages.html')

def user_profile(request):
    return render(request, 'backend/user_profile.html')

def edit_form(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_user_profile.html', {'edit_key':edit_form})

def edit_newform(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_newuser_profile.html', {'edit_key':edit_form})

# def edit_userpost(request):
#     if request.method == 'POST':
#         list_form = EditPost(request.POST, instance=request.user)
#         if list_form.is_valid():
#             list_form.save()
#             # messages.success(request, 'User edited successfully.')
#     else:
#         list_form = EditPost(instance=request.user)
#     return render(request, 'backend/add-newlisting.html', {'listf':list_form})

def reset(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            # messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/reset.html', {'pass_key':pass_form})

def pass_form(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            # messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/pass_form.html', {'pass_key':pass_form})


def list_users(request):
    show_user = User.objects.all().order_by('last_name')
    return render(request, 'backend/view-users.html', {'users':show_user})  



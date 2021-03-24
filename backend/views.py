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

 # Password Reset
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

 #  end
from frontend.models import *
from backend.forms import *

# Create your views here.


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "backend/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'leke.olamide123@gmail.com' , [user.email], fail_silently=True)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="backend/password_reset.html", context={"password_reset_form":password_reset_form})


@login_required(login_url='/backend/login/')
def dashboard(request):
    if request.user.is_staff:
        return render(request, 'backend/index.html')
    else: 
        return render(request, 'backend/user.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password, fail_silently=True)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username and Password do not match')    
    return render(request, 'frontend/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')

def success_message(request):
    return render(request, 'backend/success.html')

@login_required(login_url='/backend/login/')
# def add_newlisting(request):
#     if request.method == 'POST':
#         list_form = ListingForm(request.POST, request.FILES, fail_silently=True)
#         if list_form.is_valid():
#             listf = list_form.save(commit=False)
#             listf.user = request.user
#             listf.save()
#             return redirect('backend:add_newlisting')
            
#     else:
#         list_form = ListingForm()
#     return render(request, 'backend/add-newlisting.html', {'listf': list_form})

@login_required(login_url='/backend/login/')
def add_agent(request):
    if request.method == 'POST':
        view_form = AgentForm(request.POST, request.FILES)
        if view_form.is_valid():
            agent = view_form.save(commit=False)
            agent.user = request.user
            agent.save()
            return redirect('backend:add_agent')
            
    else:
        view_form = AgentForm()
    return render(request, 'backend/add_agent.html', {'agent': view_form})

@login_required(login_url='/backend/login/')
def agent(request):
    agent_list = Agents.objects.filter(user=request.user)
    return render(request, 'backend/agent.html', {'alist':agent_list})


@login_required(login_url='/backend/login/')
def view_agent(request, agent):
    file = get_object_or_404(Agents, pk=agent)
    return render(request, 'backend/view_agent.html', {'post':file})

@login_required(login_url='/backend/login/')
def delete_agent(request, liste_id):
    agent_record = get_object_or_404(Agents, id=liste_id)
    agent_record.delete()
    return redirect('backend:agent')



@login_required(login_url='/backend/login/')
def edit_newlisting(request, post_id):
    single_post = get_object_or_404(AddProperty, id=post_id)
    if request.method == 'POST':
        post_form = EditListing(request.POST, request.FILES, instance=single_post)
        if post_form.is_valid():
            listf = post_form.save(commit=False)
            listf.user = request.user
            listf.save()
            return redirect('backend:new_listings')
            
    else:
        post_form = EditListing(instance=single_post)
    return render(request, 'backend/edit_post.html', {'editf': post_form})


@login_required(login_url='/backend/login/')
def new_listings(request):
    hotel_list = AddProperty.objects.filter(user=request.user)
    return render(request, 'backend/newlistings.html', {'hlist':hotel_list})
    
@login_required(login_url='/backend/login/')
def view_newlistingdetails(request, pk):
    post = get_object_or_404(AddProperty, pk=pk)
    return render(request, 'backend/view-newlisting.html', {'pst':post})

@login_required(login_url='/backend/login/')
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


@login_required(login_url='/backend/login/')
def add_newlisting(request):
    if request.method == 'POST':
        list_form = ListingForm(request.POST, request.FILES)
        if list_form.is_valid():
            listf = list_form.save(commit=False)
            listf.user = request.user
            listf.save()
            return redirect('backend:add_newlisting')
    else:
        list_form = ListingForm()
    return render(request, 'backend/add-newlisting.html', {'listf': list_form})


def messages(request):
    return render(request, 'backend/messages.html')

@login_required(login_url='/backend/login/')
def user_profile(request):
    return render(request, 'backend/user_profile.html')

@login_required(login_url='/backend/login/')
def edit_form(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_user_profile.html', {'edit_key':edit_form})

@login_required(login_url='/backend/login/')
def edit_newform(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_newuser_profile.html', {'edit_key':edit_form})

@login_required(login_url='/backend/login/')
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

@login_required(login_url='/backend/login/')
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


@login_required(login_url='/backend/login/')
def list_users(request):
    show_user = User.objects.all().order_by('last_name')
    return render(request, 'backend/view-users.html', {'users':show_user})  

@login_required(login_url='/backend/login/')
def list_all_post(request):
    show_post = AddProperty.objects.all().order_by('-add_date')
    return render(request, 'backend/view-all-post.html', {'post':show_post})  

@login_required(login_url='/backend/login/')
def delete_upload(request, del_id):
    delete = get_object_or_404(AddProperty, pk= del_id)
    delete.delete()
    return redirect('backend:list_all_post')

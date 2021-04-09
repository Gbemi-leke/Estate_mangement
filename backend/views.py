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
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

 #  end
from frontend.models import *
from backend.forms import *

# signUp
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from backend.tokens import account_activation_token
from .tokens import account_activation_token
from django.template.loader import render_to_string
#end

# Create your views here.



def password_reset_request(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            # You can use more than one way like this for resetting the password.
            # ...filter(Q(email=data) | Q(username=data))
            # but with this you may need to change the password_reset form as well.
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "backend/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name':'Real Estate',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'leke.olamide123@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="backend/password_reset.html",
                  context={"password_reset_form": password_reset_form})



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
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'backend/user.html')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

def login2_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login2.html')


def logout_view(request):
    logout(request)
    return redirect('index')

def success_message(request):
    return render(request, 'backend/success.html')



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
            messages.success(request, 'Successfully edited.')

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
    if request.method  == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('backend/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')

            # messages.success(request, 'User Registered')
    else:
        form = RegisterForm()
    return render(request, 'frontend/signup.html', {'reg':form})

def activation_sent_view(request):
    return render(request, 'backend/activation_sent.html')

def activate (request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('backend:login_view')
    else:
        return render(request, 'backend/activation_invalid.html')


@login_required(login_url='/backend/login/')
def add_newlisting(request):
    if request.method == 'POST':
        list_form = ListingForm(request.POST, request.FILES)
        if list_form.is_valid():
            listf = list_form.save(commit=False)
            listf.user = request.user
            listf.save()
            messages.success(request, 'Add successfully.')
    else:
        list_form = ListingForm()
    return render(request, 'backend/add-newlisting.html', {'listf': list_form})




@login_required(login_url='/backend/login/')
def user_profile(request):
    return render(request, 'backend/user_profile.html')

@login_required(login_url='/backend/login/')
def edit_form(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit_user_profile.html', {'edit_key':edit_form})

@login_required(login_url='/backend/login/')
def edit_newform(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
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
            messages.success(request, 'Password changed successfully.')
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
            messages.success(request, 'Password changed successfully.')
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

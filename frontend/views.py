from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from backend.forms import *

# for sending mail import
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

 # Password Reset
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

 #  end

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    profile =AddProperty.objects.order_by('-add_date')[:3]
    featured=AddProperty.objects.all().filter(featured=True)[:3]
    sponsored=AddProperty.objects.all().filter(sponsored=True)[:3]
    profile2 =Agents.objects.all()[:3]
    query_form = FilterForm()
    files = {'pro':profile,'featured':featured, 'sponsored':sponsored, 'agent':profile2, 'qf':query_form }
    return render(request, 'frontend/index.html', files)

def detail_index(request, index_id):
    detail =AddProperty.objects.get(id=index_id)
    return render(request, 'frontend/detail.html', {'detail1':detail})


def filter_data(request):
    if request.method == 'GET':
        query_form = FilterForm(request.GET)
        if query_form.is_valid():
            print('Correct')
            add_price = query_form.cleaned_data.get('add_price')
            offer_type = query_form.cleaned_data.get('offer_type')
            listing_type = query_form.cleaned_data.get('listing_type')
            post = AddProperty.objects.all()
            query = AddProperty.objects.filter(offer_type=offer_type,add_price=add_price, listing_type=listing_type)
            return render(request, 'frontend/filter.html', {'q': query})
        else:
            print('Not found')
            return render(request, 'frontend/filter2.html')
    # else:
    #     query_form = FilterForm()
    # return render(request, 'frontend/filter2.html') 

def buy(request):
    # sale = AddProperty.objects.all()
    most_recent = AddProperty.objects.order_by('-add_date')
    add_post = AddProperty.objects.order_by('-add_date')
    paginated_filter = Paginator(add_post,6)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    context = {
        'person_page_obj': add_post, 
        'most_recent': most_recent
        # 'buy':sale
    }
    context['person_page_obj'] = person_page_obj
    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    return render(request, 'frontend/buy.html', context)

def detail_buy(request, buy_id):
    detail =AddProperty.objects.get(id=buy_id)
    agent_email = detail.user.email
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name+' '+email+' '+message)
        subject = 'Client Form'
        context = {'name':name, 'email':email, 'message':message }
        html_message =render_to_string('frontend/mail-template2.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'Client <leke.olamide123@gmail.com>'
        send =  mail.send_mail(subject, plain_message, from_email, [agent_email], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent sucessfully')
        else:
            messages.error(request, 'Mail not sent')
    return render(request, 'frontend/detail.html', {'det':detail})

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name+' '+email+' '+message)
        subject = 'Contact Us Form'
        context = {'name':name, 'email':email, 'message':message }
        html_message =render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <leke.olamide123@gmail.com>'
        send =  mail.send_mail(subject, plain_message, from_email, ['leke.olamide123@gmail.com'], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent sucessfully')
        else:
            messages.error(request, 'Mail not sent')

    return render(request, 'frontend/contact.html')

def contact2(request, agent_id):
    contact =Agents.objects.get(id=agent_id)
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name+' '+email+' '+message)
        subject = 'Agent Form'
        context = {'name':name, 'email':email, 'message':message }
        html_message =render_to_string('frontend/mail-template1.html', context)
        plain_message = strip_tags(html_message)
        from_email = ' Real Estate<leke.olamide123@gmail.com>'
        send =  mail.send_mail(subject, plain_message, from_email, ['leke.olamide123@gmail.com'], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent sucessfully')
        else:
            messages.error(request, 'Mail not sent')

    return render(request, 'frontend/contact2.html', {'con':contact})

def rent(request):
    # hire = AddProperty.objects.all()
    most_recent = AddProperty.objects.order_by('-add_date')
    add_post = AddProperty.objects.order_by('-add_date')
    paginated_filter = Paginator(add_post,6)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filter.get_page(page_number)
    context = {
        'person_page_obj': add_post, 
        'most_recent': most_recent
        # 'rent':hire
    }
    context['person_page_obj'] = person_page_obj
    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    return render(request, 'frontend/rent.html', context)

def detail_rent(request, rent_id):
    detail2 =AddProperty.objects.get(id=rent_id)
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name+' '+email+' '+message)
        subject = 'Client Form'
        context = {'name':name, 'email':email, 'message':message }
        html_message =render_to_string('frontend/mail-template2.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'Client <leke.olamide123@gmail.com>'
        send =  mail.send_mail(subject, plain_message, from_email, ['leke.olamide123@gmail.com', email], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent sucessfully')
        else:
            messages.error(request, 'Mail not sent')
    return render(request, 'frontend/detail.html', {'detail':detail2})

def signup(request):
    return render(request, 'frontend/signup.html')

def user(request):
    return render(request, 'frontend/user.html')


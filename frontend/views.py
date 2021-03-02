from django.shortcuts import render
from frontend.models import *


# for sending mail import
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages
# Create your views here.


def index(request):
    profile =Property.objects.all()[:4]
    featured=Property.objects.all().filter(featured=True)[:4]
    sponsored=Property.objects.all().filter(sponsored=True)[:4]
    profile2 =Agents.objects.all()
    photos = {'pro':profile,'featured':featured, 'sponsored':sponsored, 'agent':profile2 }
    return render(request, 'frontend/index.html', photos)

def buy(request):
    sale = Buy.objects.all()[:6]
    return render(request, 'frontend/buy.html', {'buy':sale})

def detail_buy(request, buy_id):
    detail =Buy.objects.get(id=buy_id)
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
        send =  mail.send_mail(subject, plain_message, from_email, ['leke.olamide123@gmail.com', email], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent sucessfully')
        else:
            messages.error(request, 'Mail not sent')

    return render(request, 'frontend/contact2.html', {'con':contact})

def rent(request):
    hire = Rent.objects.all()[:6]
    return render(request, 'frontend/rent.html', {'rent':hire})

def detail_rent(request, rent_id):
    detail2 =Rent.objects.get(id=rent_id)
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
    return render(request, 'frontend/details.html', {'detail':detail2})

def signup(request):
    return render(request, 'frontend/signup.html')

def user(request):
    return render(request, 'frontend/user.html')
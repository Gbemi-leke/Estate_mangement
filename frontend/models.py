from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Agents(models.Model):
    agent_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    agent_title = models.CharField(max_length=100, verbose_name='Profile Title')
    agent_desription = models.TextField(verbose_name='Description')
    agent_contact = models.CharField(max_length=20, verbose_name='Contact')
    agent_address = models.CharField(max_length=100, verbose_name='Address')
    agent_email = models.EmailField(max_length=50, verbose_name='Email')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Agents'


    def __str__(self):
        return self.agent_title




class AddProperty(models.Model):

    SPONSORED = "S"
    FEATURED = "F"
    BUY = "B"
    RENT = "R"
    CHOOSE = ""

    PROPERTY_TYPE = [
        (SPONSORED, 'Sponsored'),
        (FEATURED, 'Featured'),
        (BUY, 'Buy'),
        (RENT, 'Rent'),
        (CHOOSE, 'Please Choose')

    ]
    
    add_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/' )
    add_title = models.CharField(max_length=100, verbose_name='Profile Title')
    add_price = models.IntegerField(verbose_name='Price')
    add_desription = models.TextField(verbose_name='Description')
    add_contact = models.CharField(max_length=20, verbose_name='Contact')
    add_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE, default=CHOOSE)

    class Meta():
        verbose_name_plural = 'AddProperty'
        
    def __str__(self):
        return self.add_title


class Location(models.Model):
    location_name = models.CharField(max_length=100, verbose_name='Location Nmae')

    def __str__(self):
        return self.location_name

    class Meta():
        verbose_name_plural= "Property Location"

class UserProfile(models.Model):
    user_image = models.FileField(null=True, verbose_name='User Image', blank=True, upload_to='uploads/')
    username = models.CharField(max_length=150, verbose_name= 'User Name')
    first_name = models.CharField(max_length=150, verbose_name= 'First Name')
    second_name = models.CharField(max_length=150, verbose_name= 'Second Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    tel = models.CharField(max_length=20, verbose_name= 'Founder Number')
    email = models.EmailField(max_length=150, verbose_name= 'Founder Email')

    def __str__(self):
        return self.username


    class Meta():
        verbose_name_plural= "UserProfile"
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Property(models.Model):
    
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
    pro_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    pro_title = models.CharField(max_length=100, verbose_name='Profile Title')
    pro_sale = models.CharField(max_length=20, verbose_name='Sales or Rent')
    pro_price = models.CharField(max_length=20, verbose_name='Price')
    pro_desription = models.TextField(verbose_name='Description')
    pro_contact = models.CharField(max_length=20, verbose_name='Contact')
    pro_date = models.DateTimeField(auto_now_add=True)
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE, default=CHOOSE)

    class Meta():
        verbose_name_plural = 'Property'

    def __str__(self):
        return self.pro_title

    def post_img(self):
        if self.pro_img:
          return self.pro_img.url


class Agents(models.Model):
    agent_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    agent_title = models.CharField(max_length=100, verbose_name='Profile Title')
    agent_desription = models.TextField(verbose_name='Description')
    agent_contact = models.CharField(max_length=20, verbose_name='Contact')
    agent_address = models.CharField(max_length=100, verbose_name='Address')
    agent_email = models.EmailField(max_length=50, verbose_name='Email')

    class Meta():
        verbose_name_plural = 'Agents'


    def __str__(self):
        return self.agent_title


class Profile(models.Model):
    image = models.FileField()


class AddProperty(models.Model):

    BUY = "B"
    RENT = "R"
    CHOOSE = ""

    PROPERTY_TYPE = [
        (BUY, 'Buy'),
        (RENT, 'Rent'),
        (CHOOSE, 'Please Choose')

    ]
    add_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    add_title = models.CharField(max_length=100, verbose_name='Profile Title')
    add_price = models.CharField(max_length=20, verbose_name='Price')
    add_desription = models.TextField(verbose_name='Description')
    add_contact = models.CharField(max_length=20, verbose_name='Contact')
    add_date = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE, default=CHOOSE)

    class Meta():
        verbose_name_plural = 'AddProperty'
        
    def __str__(self):
        return self.add_title


    
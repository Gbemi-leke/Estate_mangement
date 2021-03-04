from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Property(models.Model):
    pro_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    pro_title = models.CharField(max_length=100, verbose_name='Profile Title')
    pro_sale = models.CharField(max_length=20, verbose_name='Sales or Rent')
    pro_price = models.CharField(max_length=20, verbose_name='Price')
    pro_desription = models.TextField(verbose_name='Description')
    pro_contact = models.CharField(max_length=20, verbose_name='Contact')
    pro_date = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    sponsored = models.BooleanField()

    class Meta():
        verbose_name_plural = 'Property'

    def __str__(self):
        return self.pro_title


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



class Buy(models.Model):
    buy_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    buy_title = models.CharField(max_length=100, verbose_name='Profile Title')
    buy_price = models.CharField(max_length=20, verbose_name='Price')
    buy_desription = models.TextField(verbose_name='Description')
    buy_contact = models.CharField(max_length=100, verbose_name='Contact')
    buy_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Buy'


    def __str__(self):
        return self.buy_title

    def post_img(self):
        if self.buy_image:
          return self.buy_image.url

class Rent(models.Model):
    rent_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    rent_title = models.CharField(max_length=100, verbose_name='Profile Title')
    rent_price = models.CharField(max_length=20, verbose_name='Price')
    rent_desription = models.TextField(verbose_name='Description')
    rent_contact = models.CharField(max_length=100, verbose_name='Contact')
    rent_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Rent'


    def __str__(self):
        return self.rent_title


class Profile(models.Model):
    image = models.FileField()


class AddProperty(models.Model):
    pro_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    pro_title = models.CharField(max_length=100, verbose_name='Profile Title')
    pro_sale = models.CharField(max_length=20, verbose_name='Sales or Rent')
    pro_price = models.CharField(max_length=20, verbose_name='Price')
    pro_desription = models.TextField(verbose_name='Description')
    pro_contact = models.CharField(max_length=20, verbose_name='Contact')
    pro_date = models.DateTimeField(auto_now_add=True)
    buy = models.BooleanField()
    rent = models.BooleanField()

    class Meta():
        verbose_name_plural = 'AddProperty'


    def __str__(self):
        return self.pro_title




    
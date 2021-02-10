from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Property(models.Model):
    pro_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    pro_title = models.CharField(max_length=100, verbose_name='Profile Title')
    pro_price = models.DecimalField(max_digits=10, verbose_name= 'Price', decimal_places=2)
    pro_desription = models.TextField(verbose_name='Description')
    pro_date = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    sponsored = models.BooleanField()

    class Meta():
        verbose_name_plural = 'Property'

    def post_img(self):
        if self.pro_img:
            return self.pro_img.url

    def __str__(self):
        return self.pro_title


class Agents(models.Model):
    agent_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    agent_title = models.CharField(max_length=100, verbose_name='Profile Title')
    agent_desription = models.TextField(verbose_name='Description')

    class Meta():
        verbose_name_plural = 'Agents'


    def __str__(self):
        return self.agent_title



class Buy(models.Model):
    buy_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    buy_title = models.CharField(max_length=100, verbose_name='Profile Title')
    buy_price = models.DecimalField(max_digits=10, verbose_name= 'Price', decimal_places=2)
    buy_desription = models.TextField(verbose_name='Description')
    buy_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Buy'


    def __str__(self):
        return self.buy_title

class Rent(models.Model):
    rent_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    rent_title = models.CharField(max_length=100, verbose_name='Profile Title')
    rent_price = models.DecimalField(max_digits=10, verbose_name= 'Price', decimal_places=2)
    rent_desription = models.TextField(verbose_name='Description')
    rent_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Rent'


    def __str__(self):
        return self.rent_title
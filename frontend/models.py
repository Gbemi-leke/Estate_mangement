from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    f_name = models.CharField(max_length=100, verbose_name='First name')
    l_name = models.CharField(max_length=100, verbose_name='Last name')
    username = models.CharField(max_length=100, verbose_name='User name')
    email = models.CharField(max_length=100, verbose_name='Email')

    def __str__(self):
        return self.username

class Category(models.Model):
    for_sale = models.CharField(blank=True, null=True, max_length=100, verbose_name='Sale or rent')
    

    def __str__(self):
        return self.for_sale

    class Meta():
        verbose_name_plural='Category'

class Sale(models.Model):
    pst_img = models.ImageField(null=True, verbose_name='Image 1', blank=True, upload_to='uploads/')
    pst_img = models.ImageField(null=True, verbose_name='Image 2', blank=True, upload_to='uploads/')
    pst_img = models.ImageField(null=True, verbose_name='Image 3', blank=True, upload_to='uploads/')
    pst_title = models.CharField(max_length=100, verbose_name='Type of property')
    price = models.PositiveIntegerField(verbose_name='Price',)
    cat_id = models.ManyToManyField(Category, verbose_name='Category')
    bath = models.PositiveIntegerField(verbose_name='Num of Bathrooms',)
    restroom = models.PositiveIntegerField(verbose_name='Num of Toilets',)
    more = models.CharField(max_length=100, verbose_name='More information')





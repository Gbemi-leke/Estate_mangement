from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    f_name = models.CharField(max_length=150, verbose_name='First name')
    l_name = models.CharField(max_length=150, verbose_name='Last name')
    email = models.CharField(max_length=150, verbose_name='Email')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(null=True, verbose_name='Image', blank=True, upload_to='uploads/')

    def __str__(self):
        return self.user.username

# class SalePost(models.Model):
#     pst_image = models.ImageField(null=True, verbose_name='House Image', blank=True, upload_to='uploads/')
#     pst_title = models.CharField(max_length=150, verbose_name='')
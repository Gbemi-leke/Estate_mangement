from django.db import models

# Create your models here.
class Sponsored(models.Model):
    spon_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/')
    spon_title = models.CharField(max_length=100, verbose_name='Profile Title')
    spon_price = models.DecimalField(max_digits=10, verbose_name= 'Price', decimal_places=2)
    spon_desription = models.TextField(verbose_name='Description')
    spon_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Sponsored'


    def __str__(self):
        return self.spon_title


class Latest(models.Model):
    lat_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/')
    lat_title = models.CharField(max_length=100, verbose_name='Profile Title')
    lat_price = models.DecimalField(max_digits=10, verbose_name= 'Price', decimal_places=2)
    lat_desription = models.TextField(verbose_name='Description')
    lat_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Latest'


    def __str__(self):
        return self.lat_title

class Featured(models.Model):
    fat_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/')
    fat_title = models.CharField(max_length=100, verbose_name='Profile Title')
    fat_price = models.DecimalField(max_digits=10, verbose_name= 'Price', decimal_places=2)
    fat_desription = models.TextField(verbose_name='Description')
    fat_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Featured'


    def __str__(self):
        return self.fat_title
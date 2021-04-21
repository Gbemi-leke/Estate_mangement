from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

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
    BUY = "B"
    RENT = "R"
    CHOOSE = ""

    OFFER_TYPE = [
        (BUY, 'Buy'),
        (RENT, 'Rent'),
        (CHOOSE, 'Please Choose')

    ]


    BUNGALOW = "Bungalow"
    DUPLEX = "Duplex"
    FLAT = "Flat"
    GLASSHOUSE = "Glasshouse"
    STORY_BUILDING = "Story Building"
    CHOOSE = ""

    PROPERTY_TYPE = [

        (BUNGALOW, 'Bungalow'),
        (DUPLEX, 'Duplex'),
        (FLAT, 'Flat'),
        (GLASSHOUSE, 'Glass House'),
        (STORY_BUILDING, 'Story Building'),
        (CHOOSE, 'Please Choose')

    ]


    ONE = "100,000"
    TWO = "150,00"
    THREE = "200,000"
    FOUR = "250,000"
    FIVE = "300,000"
    SIX = "350,000"
    SEVEN = "400,000"
    EIGHT = "450,000"
    NINE = "500,000"
    TEN = "550,000"
    ONE1 = "600,000"
    TWO2 = "650,000"
    THREE3 = "700,000"
    FOUR4 = "750,000"
    FIVE5 = "800,000"
    SIX6 = "850,000"
    SEVEN7 = "900,000"
    EIGHT8 = "950,000"
    NINE9 = "1 Million"
    TEN10 = "1.5 Million"
    ONE11 = "2 Million"
    TWO22 = "2.5 Million"
    THREE33 = "3 Million"
    FOUR44 = "3.5 Million"
    FIVE55 = "4 Million"
    SIX66 = "4.5 Million"
    SEVEN77= "5 Million"
    CHOOSE = ""

    PRICE= [
         (ONE, ' 100,000'),
         (TWO, ' 150,000'),
         (THREE, ' 200,000'),
         (FOUR, ' 250,000'),
         (FIVE, ' 300,000'),
         (SIX, ' 350,000'),
         (SEVEN, ' 400,000'),
         (EIGHT, ' 450,000'),
         (NINE, ' 500,000'),
         (TEN, ' 550,000'),
         (ONE1, ' 600,000'),
         (TWO2, ' 650,000'),
         (THREE3, ' 700,000'),
         (FOUR4, ' 750,000'),
         (FIVE5, ' 800,000'),
         (SIX6, ' 850,000'),
         (SEVEN7, ' 900,000'),
         (EIGHT8, ' 950,000'),
         (NINE9, ' 1 Million'),
         (TEN10, ' 1.5 Million'),
         (ONE11, ' 2 Million'),
         (TWO22, ' 2.5 Million'),
         (THREE33, ' 3 Million'),
         (FOUR44, ' 3.5 Million'),
         (FIVE55, ' 4 Million'),
         (SIX66, ' 4.5 Million'),
         (SEVEN77, ' 5 Million'),
         (CHOOSE, 'Please Choose')
    ]
    add_img = models.ImageField(blank=True, verbose_name='Property image', null=True, upload_to='uploads/' )
    img1 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    img2 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    img3 = models.ImageField(blank=True, verbose_name='Other Images', null=True, upload_to='uploads/' )
    add_title = models.CharField(max_length=100, verbose_name='Property Name')
    add_price = models.CharField(max_length=40, choices=PRICE, default=CHOOSE)
    listing_type = models.CharField(max_length=40, choices=PROPERTY_TYPE, default=CHOOSE)
    add_desription = models.TextField(verbose_name='Description')
    add_contact = models.CharField(max_length=20, verbose_name='Contact')
    add_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_type = models.CharField(max_length=40, choices=OFFER_TYPE, default=CHOOSE)
    sponsored =models.BooleanField()
    featured = models.BooleanField()


    class Meta():
        verbose_name_plural = 'AddProperty'

    def __str__(self):
        return self.add_title

    def img_url(self):
        if self.add_img:
            return self.add_img.url

    def img1_url(self):
        if self.img1:
            return self.img1.url

    def img2_url(self):
        if self.img2:
            return self.img2.url

    def img3_url(self):
        if self.img3:
            return self.img3.url




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


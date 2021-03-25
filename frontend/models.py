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
    add_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/' )
    add_title = models.CharField(max_length=100, verbose_name='Profile Title')
    add_price = models.CharField(max_length=40, choices=PRICE, default=CHOOSE)
    listing_type = models.CharField(max_length=40, choices=PROPERTY_TYPE, default=CHOOSE)
    add_desription = models.TextField(verbose_name='Description')
    add_contact = models.CharField(max_length=20, verbose_name='Contact')
    add_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_type = models.CharField(max_length=40, choices=OFFER_TYPE, default=CHOOSE)
    sponsored = models.BooleanField(default=False, blank=True)
    featured = models.BooleanField(default=False, blank=True)
    

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
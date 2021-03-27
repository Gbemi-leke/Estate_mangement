from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email*', widget=forms.EmailInput
        (attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    phone = forms.CharField(label='Tel*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    password1 = forms.CharField(label='Enter Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    # pst_image = forms.FileField(required=False)

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = [ 'first_name','last_name','username', 'email', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        # user.pst_image = self.cleaned_data['pst_image']

        if commit:
            user.save()
            return user


class EditUserForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Username' }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))

    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))


    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', ]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),

            'first_name': forms.TextInput(attrs={'class':'form-control'}),

            'last_name': forms.TextInput(attrs={'class':'form-control'}),

            'email':forms.TextInput(attrs={'class':'form-control'}),

            'phone': forms.NumberInput(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.agent_img = self.cleaned_data['agent_img']


        if commit:
            user.save()
            return user

class ListingForm(forms.ModelForm):

    class Meta():
        model = AddProperty
        fields = ['add_title', 'add_img', 'add_price','add_contact','add_desription','listing_type','sponsored','featured', 'offer_type',]
        exclude = ['date', 'user']
        widgets = {
            'add_img': forms.FileInput(attrs={'class': 'form-control'}),
            'add_title': forms.TextInput(attrs={'class': 'form-control'}),
            'add_price': forms.Select(attrs={'class': 'form-control'}),
            'listing_type': forms.Select(attrs={'class': 'form-control'}),
            'add_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'add_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'offer_type' : forms.Select(attrs={'class': 'form-control'}),


        }


class EditListing(forms.ModelForm):

    class Meta():
        model = AddProperty
        exclude = ['date', 'user']

        widgets = {
            'add_img': forms.FileInput(attrs={'class': 'form-control'}),
            'add_title': forms.TextInput(attrs={'class': 'form-control'}),
            'add_price': forms.Select(attrs={'class': 'form-control'}),
            'listing_type': forms.Select(attrs={'class': 'form-control'}),
            'add_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'add_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'offer_type' : forms.Select(attrs={'class': 'form-control'}),


        }

class PasswordChangeForm(PasswordChangeForm):

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1', 'password2']

        widgets = {
                'password1': forms.NumberInput(attrs={'class': 'form-control'}),
                'password2': forms.NumberInput(attrs={'class': 'form-control'}),

            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
            return user


class AgentForm(forms.ModelForm):

    class Meta():
        model = Agents
        fields = ['agent_title', 'agent_img','agent_contact','agent_desription','agent_address','agent_email']
        exclude = ['user']

        widgets = {
            'agent_img': forms.FileInput(attrs={'class': 'form-control'}),
            'agent_title': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'agent_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class EditAgent(forms.ModelForm):

    class Meta():
        model = Agents
        exclude = ['user']

        widgets = {
            'agent_img': forms.FileInput(attrs={'class': 'form-control'}),
            'agent_title': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'agent_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_email': forms.EmailInput(attrs={'class': 'form-control'}),

        }



class FilterForm(forms.ModelForm):
    BUY = "B"
    RENT = "R"
    CHOOSE = ""

    OFFER_TYPE = [
        (BUY, 'Buy'),
        (RENT, 'Rent'),
        (CHOOSE, 'Offer Type')

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
        (CHOOSE, 'Property Type')

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
         (CHOOSE, 'Price')
    ]
    # add_title = forms.CharField(required=False, label='Location*', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Location'}))

    add_price = forms.CharField(required=False, label='Price*', widget=forms.Select(choices=PRICE,
        attrs={'class': 'form-control', 'placeholder': 'Price'}))

    listing_type = forms.CharField(required=False, label='Property Type*', widget=forms.Select(choices=PROPERTY_TYPE,
        attrs={'class': 'form-control', 'placeholder': 'Property Type'}))

    offer_type = forms.CharField(required=False, label='Offer Type*', widget=forms.Select(choices=OFFER_TYPE,
        attrs={'class': 'form-control', 'placeholder': 'Offer Type'}))

    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(), empty_label='Please Choose',
    #     widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta():
        fields = ['listing_type', 'offer_type']
        model = AddProperty
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

    agent_img = forms.FileField(required=False)

    
    

    # botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
    #                            validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = Agents
        fields = ['agent_img']

    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', ]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),

            'first_name': forms.TextInput(attrs={'class':'form-control'}),

            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            
            'email':forms.TextInput(attrs={'class':'form-control'}),

            'phone': forms.NumberInput(attrs={'class':'form-control'}),

            'agent_img': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.agent_img = self.cleaned_data['agent_img']

        # user.description = self.cleaned_data['description']
    
        if commit:
            user.save()
            return user

class ListingForm(forms.ModelForm):

    class Meta():
        model = AddProperty
        fields = ['add_title', 'add_img', 'add_price','add_contact','add_desription','listing_type', 'property_type',]
        exclude = ['date', 'user']
        widgets = { 
            'add_img': forms.FileInput(attrs={'class': 'form-control'}),
            'add_title': forms.TextInput(attrs={'class': 'form-control'}),
            'add_price': forms.TextInput(attrs={'class': 'form-control'}),
            'listing_type': forms.TextInput(attrs={'class': 'form-control'}),
            'add_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'add_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type' : forms.Select(attrs={'class': 'form-control'}),
            
            
        }


class EditListing(forms.ModelForm):

    class Meta():
        model = AddProperty
        exclude = ['date', 'user']

        widgets = { 
            'add_img': forms.FileInput(attrs={'class': 'form-control'}),
            'add_title': forms.TextInput(attrs={'class': 'form-control'}),
            'add_price': forms.TextInput(attrs={'class': 'form-control'}),
            'listing_type': forms.TextInput(attrs={'class': 'form-control'}),
            'add_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'add_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type' : forms.Select(attrs={'class': 'form-control'}),
            
            
        }

class PasswordChangeForm(PasswordChangeForm):

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1' 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        
        if commit:
            user.save()
            return user


# class ListingForm(forms.ModelForm):
#     class Meta():
#         model = AddProperty
#         exclude = ['add_date', 'user']


class FilterForm(forms.ModelForm):
    add_title = forms.CharField(required=False, label='Location*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Location'}))

    add_price = forms.CharField(required=False, label='Price*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Price'}))

    listing_type = forms.CharField(required=False, label='Listing Type*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Listing Type'}))

    # property_type =forms.ModelChoiceField(required=False, 
    #     queryset=AddProperty.objects.order_by('property_type'), empty_label='Please Choose', 
    #     widget=forms.Select( attrs={'class': 'form-control',}))

    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(), empty_label='Please Choose',
    #     widget=forms.Select(attrs={'class': 'form-control'}))
   
    class Meta():
        exclude = ['add_date','add_desription','add_img','add_contact']
        model = AddProperty
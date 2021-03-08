from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email*',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
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
        fields = [ 'first_name','last_name','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
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

    pst_image = forms.FileField(required=False)
    

    # botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
    #                            validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', 'pst_image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.pst_image = self.cleaned_data['pst_image']

        # user.description = self.cleaned_data['description']
    
        if commit:
            user.save()
            return user

# class PictureForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields =('image',)

class PasswordChangeForm(PasswordChangeForm):

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        
        if commit:
            user.save()
            return user

        

class ListingForm(forms.ModelForm):
    class Meta():
        model = AddProperty
        exclude = ['date', 'user']


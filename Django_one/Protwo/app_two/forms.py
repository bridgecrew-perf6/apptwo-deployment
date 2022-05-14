from dataclasses import field
from pyexpat import model
from django import forms
# from django.contrib.auth.forms import Authentication
from django.contrib.auth.models import User
from app_two.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        
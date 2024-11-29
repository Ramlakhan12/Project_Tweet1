from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from . models import *
from django import forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class TweetFrom(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','image']

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1')
        
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Messageform(forms.ModelForm):

    class Meta:
        model = Message
        widgets = {
            'content': forms.Textarea(attrs={'rows': 1, 'cols': 35}),
        }
        fields = ['content']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

from .models import *
from django import forms
from django.contrib.auth.models import User


class Messageform(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content']


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', ]

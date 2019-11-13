from .models import *
from django import forms

class Messageform(forms.ModelForm):

   class Meta:
       model = Message
       fields = ['content']
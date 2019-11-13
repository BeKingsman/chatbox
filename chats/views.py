from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def homepage(request):
    users = User.objects.all()

    return render(request, 'home.html', {'users': users})


def Chat(request, pk):
    if(request.method == 'POST'):
        form = Messageform(request.POST)
        form.instance.m_sent_to = User.objects.get(pk=pk)
        form.instance.sent_by = request.user
        if (form.is_valid):
            form.save()

    form = Messageform()

    return render(request, 'message.html', {'form': form})


def user_login(request):
    pass


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()

    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

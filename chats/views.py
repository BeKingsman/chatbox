from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):
    users = User.objects.all()

    return render(request, 'home.html', {'users': users})


@login_required
def Chat(request, pk):

    all_mess = Message.objects.filter(m_sent_to=request.user, sent_by=User.objects.get(pk=pk))
    messages_sent = Message.objects.filter(sent_by=request.user, m_sent_to=User.objects.get(pk=pk))
    mess_list = all_mess | messages_sent  # combined list
    message_list = mess_list.order_by('time')

    if request.method == 'POST':
        form = Messageform(request.POST)
        form.instance.m_sent_to = User.objects.get(pk=pk)
        form.instance.sent_by = request.user
        if form.is_valid:
            form.save()

    form = Messageform()

    return render(request, 'message.html', {'form': form, 'all_mess': all_mess, 'id': pk, 'messages_sent': messages_sent, 'mess_list': mess_list, 'message_list': message_list})


def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if(authenticate(username=username, password=password)):
            user = authenticate(username=username, password=password)

            login(request, user)
        return redirect('home')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

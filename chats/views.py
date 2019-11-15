from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def homepage(request):
    users = User.objects.all()

    return render(request, 'home.html', {'users': users})


@login_required
def Chat(request, pk):

    all_mess = Message.objects.filter(m_sent_to=request.user, sent_by=User.objects.get(pk=pk))
    messages_sent = Message.objects.filter(sent_by=request.user, m_sent_to=User.objects.get(pk=pk))
    mess_list = all_mess | messages_sent  # combined list
    message_list = (mess_list.order_by('time')).reverse()

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
        u_form = UserRegisterForm(data=request.POST)
        p_form = ProfileForm(data=request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            user.save()

            p1 = p_form.save(commit=False)
            p1.user = user

            if 'image' in request.FILES:
                p1.image = request.FILES['image']

            p1.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('login')

        else:
            print(u_form.errors, p_form.errors)
            return HttpResponse('<h1> Karta reh koshish </h1>')

    else:
        u_form = UserRegisterForm()
        p_form = ProfileForm()
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'register.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserProfileInfoForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserProfileInfoForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

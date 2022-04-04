from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfilerForm
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password= password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()

    context = {
        'title': 'Geekshop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Регистрация прошлв успешно')
            return HttpResponseRedirect(reverse('authapp:login'))

    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop | Регистрация',
        'form' : form
    }
    return render(request, 'authapp/register.html', context)

def profile(request):

    if request.method == 'POST':
        form = UserProfilerForm(instance=request.user,data=request.POST)
        if form.is_valid():
            messages.success(request,'Ваши данные изменены')
            form.save()
        else:
            messages.error(request, form.errors)




    context = {
        'title': 'Geekshop | Данные пользователя',
        'form': UserProfilerForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'authapp/profile.html', context)

def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from Users.forms import LoginForm, RegisterForm


def logout_users(request):
    logout(request)
    return redirect('login')


def login_users(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cred = form.cleaned_data
            user = authenticate(request, username=cred['username'], password=cred['password'])
            if user or user.is_active():
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()

    data = {
        'title': 'Авторизация',
        'header': 'Добро пожаловать на страницу авторизации',
        'form': form,
    }
    return render(request, 'Users/login_users.html', context=data)


def register_users(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    else:
        form = RegisterForm()

    data = {
        'title': 'Регистрация',
        'header': 'Добро пожаловать на страницу регистрации',
        'form': form,
    }
    return render(request, 'Users/register_users.html', context=data)
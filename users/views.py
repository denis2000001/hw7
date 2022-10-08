from django.shortcuts import render, redirect
from users.forms import RegiserForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import render
from users.forms import RegisterForm, LoginForm, SetPassForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from posts.views import get_user_from_request
# Create your views here.

def register_view(request):
    if request.method == "GET":
        return render(request, "users/register.html", context={'form': RegisterForm})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )
            return redirect('/users/login/')
    else:
        return render(request, 'users/register.html', context={'form': form})

def set_password(request, id):
    if request.method == 'GET':
        return render(request, 'users/change.html', context={
            'pers': SetPassForm,
            'id': id
        })
    elif request.method == 'POST':
        form = SetPassForm(request.POST)
        user = User.objects.get(id=id)
        if form.is_valid():
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('/')
        else:
            return render(request, 'users/change.html', context={
                'pers': SetPassForm,
                'id': id
            })


def login_view(request):
    if request.method == "GET":
        return render(request, 'users/login.html', context={'form': LoginForm})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/')
        else:
            return render(request, 'users/login.html', context={'form': form})

def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect('/')

def personal_info(request):
    if request.method == 'GET':
        if get_user_from_request(request):
            return render(request, 'users/personal.html', context={'user': request.user})
        else:
            return redirect('/')
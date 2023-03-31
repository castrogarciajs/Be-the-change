"""django."""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


def main(request):
    """main."""
    title = 'Be Me Change !'
    return render(request, 'index.html', {
        'title': title,
    })


def register(request):
    """Register."""
    title = 'Register'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password_confirm = request.POST['password2']

        if password == password_confirm:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'auth/Register.html', {
                    'title': title,
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'auth/Register.html', {
            'title': title,
            'form': UserCreationForm,
            'error': 'La contraseña no coincide'
        })

    return render(request, 'auth/Register.html', {
        'title': title,
        'form': UserCreationForm
    })


def singout(request):
    """logout."""
    logout(request)
    return redirect('main')


def login_user(request):
    """login."""
    title = 'Login'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            render(request, 'auth/Login.html', {
                'title': title,
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('tasks')

    return render(request, 'auth/Login.html', {
        'title': title,
        'form': AuthenticationForm
    })


def tasks(request):
    """Tasks."""
    title = 'Tasks'
    return render(request, 'pages/Tasks.html', {
        'title': title
    })

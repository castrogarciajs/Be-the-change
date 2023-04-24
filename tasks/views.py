"""django."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateTask
from .models import Task

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
    tasks = Task.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'pages/Tasks.html', {
        'title': title,
        'tasks': tasks
    })


def save_task(request):
    """Created."""
    title = 'Sv - Task'
    if request.method == 'POST':
        try:
            form = CreateTask(request.POST)
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
        except ValueError:
            print("Hubo un error")
            return ValueError
    return render(request, 'pages/Create_Task.html', {
        'title': title,
        'form': CreateTask,
    })


def task_by_id(request, id):
    title = f"Task - By {id}"
    task = get_object_or_404(Task, pk=id)
    return render(request, 'pages/id_task.html', {
        'title': title,
        'task': task
    })

"""django."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateTask
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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


@login_required
def tasks(request):
    """Tasks."""
    title = 'Tasks'
    tasks = Task.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'pages/Tasks.html', {
        'title': title,
        'tasks': tasks
    })


@login_required
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


@login_required
def task_by_id(request, id):
    title = f"Task - By {id}"
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=id, user=request.user)
        form = CreateTask(instance=task)
        return render(request, 'pages/id_task.html', {
            'title': title,
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=id, user=request.user)
            form = CreateTask(request.POST, instance=task)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(request, 'pages/id_task.html', {
                'title': title,
                'task': task,
                'form': form,
                'error': 'hubo un error actulizando'
            })


@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.completed = timezone.now()
        task.save()
        return redirect("tasks")


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect("tasks")


@login_required
def tasks_completed(request):
    """Tasks."""
    title = 'Tasks'
    tasks = Task.objects.filter(
        user=request.user, completed__isnull=False).order_by('-completed')
    return render(request, 'pages/Tasks.html', {
        'title': title,
        'tasks': tasks
    })

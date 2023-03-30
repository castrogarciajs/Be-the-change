"""django."""
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                return HttpResponse('USER SUCCESFULLY')
            except ValueError as error_message:
                print(error_message)
                return HttpResponse('USER EXISTS')

        return HttpResponse('PASSWORD NOT MATCH')

    return render(request, 'auth/Register.html', {
        'title': title,
        'form': UserCreationForm
    })

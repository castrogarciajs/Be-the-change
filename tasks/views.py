"""django."""
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def main(request):
    """main."""
    title = 'Register'
    return render(request,'auth/Register.html', {
        'title': title,
        'form': UserCreationForm
    })
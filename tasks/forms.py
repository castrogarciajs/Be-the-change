from django.forms import ModelForm
from .models import Task

class CreateTask(ModelForm):
    class meta:
        model = Task
        fields = ['title', 'description', 'important']
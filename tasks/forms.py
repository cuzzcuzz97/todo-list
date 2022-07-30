
from django import forms 

from .models import TaskList

class TasksForm(forms.ModelForm):
    title = forms.CharField(max_length=64)
    detail = forms.CharField(max_length=64)

    class Meta:
        model = TaskList
        fields = '__all__'
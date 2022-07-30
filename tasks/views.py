from django.shortcuts import render
from .models import TaskList
from django.http import HttpResponse , HttpResponseRedirect
from .forms import TasksForm
from django.urls import reverse
# Create your views here.

# def index(request):
#     return HttpResponse("You're looking at tasks' list")

def tasks(request):
    tasklist = TaskList.objects.all()
    context = {
        'tasks' : tasklist
    }
    return render(request, 'tasks/tasks.html', context)

def formtasks(request):
    context = {}
    tasklist = TaskList.objects.all()
    form = TasksForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tasks'))

    return render(request, 'tasks/form.html', {'form' : form,
    'tasks':  tasklist
    })

def delete(request, id):
    task = TaskList.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('tasks'))
from django.shortcuts import render
from .models import TaskList
from django.http import HttpResponse , HttpResponseRedirect
from .forms import TasksForm
from django.urls import reverse
from django.shortcuts import redirect

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

def complete(request, id):
    task = TaskList.objects.get(id=id)
    if task.complete == True:
        task.complete = False
        task.save()
    else:
        task.complete = True
        task.save()
    return HttpResponseRedirect(reverse('tasks'))

def update(request, id):
    task = TaskList.objects.get(id=id)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TasksForm(instance=task)

    return render(request, 'tasks/update.html', {'form': form})
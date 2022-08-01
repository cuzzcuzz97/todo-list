from django.shortcuts import render
from .models import TaskList
from django.http import HttpResponse , HttpResponseRedirect
from .forms import TasksForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





# Create your views here.

# def index(request):
#     return HttpResponse("You're looking at tasks' list")

def tasks(request):
    if not request.user.is_authenticated:
        return redirect('login')
    tasklist = TaskList.objects.filter(user=request.user)
    context = {
        'tasks' : tasklist
    }
    return render(request, 'tasks/tasks.html', context)

def formtasks(request):

    if not request.user.is_authenticated:
        return redirect(tasks)
    context = {}
    # tasklist = TaskList.objects.all()
    form = TasksForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('tasks'))

    return render(request, 'tasks/form.html', {'form' : form,
    # 'tasks':  tasklist
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


def login_view(request):
    if request.user.is_authenticated:
        return redirect('tasks')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('tasks')
    else:
        messages.error(request, "Wrong Creadential")
        return render(request, 'tasks/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    
    if request.user.is_authenticated:
        return redirect('tasks')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('tasks')

        else:
            return render(request, 'tasks/signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'tasks/signup.html', {'form': form})


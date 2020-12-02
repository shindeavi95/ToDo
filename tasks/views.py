from django.shortcuts import render,redirect
from .models import *
from .form import *


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    data= {'tasks':tasks, 'form':form}
    return render(request,'tasks/list.html',data)

def updateTask(request, pk):

             task = Task.objects.get(id=pk)
             form = TaskForm(instance=task)
             if request.method == 'POST':
                 form = TaskForm(request.POST, instance=task)
                 if form.is_valid():
                     form.save()
                    return redirect('/')
             data = {'form':form}

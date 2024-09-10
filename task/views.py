from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task_list
from .forms import CreateTask, UpdateTask, DeleteTask

# Create your views here.
def main(request):
    return render(request, 'main.html')

def task(request):
    projects = list(Task_list.objects.values())
    return render(request, 'task.html', {
        'projects' : projects
    })

def create_tasks(request):
    if request.method == "GET":
        return render(request, 'crear_tasks.html',{
            'form': CreateTask()
        })
    else:    
        Task_list.objects.create(name= request.POST['name'], description = request.POST['description'] ,date_end= request.POST['date_end'])
        return redirect('/Tareas')
    
def task_detail(request, id):
    task = get_object_or_404(Task_list, id=id)
    task_data = {
        'id': task.id,
        'name': task.name,
        'description': task.description,
        'date_start': task.date_start,
        'date_end': task.date_end,
        'hour_end': task.hour_end,
        'completada': task.completada,
    }
        


def update_task(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task_list, id = id)
        return render(request, 'update_task.html',{
            'form': UpdateTask()
        })
    else:
        form = UpdateTask(request.POST)
        if form.is_valid():
            task_id = form.cleaned_data['task_id']
            task = get_object_or_404(Task_list, id=task_id)
            task.name = form.cleaned_data['name']
            task.description = form.cleaned_data['description']
            task.date_end = form.cleaned_data['date_end']
            task.save()
        return redirect('/Tareas')
    #return render(request, 'update_task.html')

def delete_tasks(request, id):
    if request.method == 'GET':
        task = Task_list.objects.get(id= id)
        return render(request, 'delete_task.html',{
            'form' : DeleteTask()
        })
    else:
        form = DeleteTask(request.POST)
        if form.is_valid():
            task_id = form.cleaned_data['task_id']
            task = get_object_or_404(Task_list, id=task_id)
            task.delete()
        return redirect('/Tareas')

    
def create_tasks(request):
    if request.method == "GET":
        return render(request, 'crear_tasks.html',{
            'form': CreateTask()
        })
    else:    
        Task_list.objects.filter()(name= request.POST['name'], description = request.POST['description'] ,date_end= request.POST['date_end'])
        return redirect('/Tareas')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
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


def delete_tasks(request, id):    
    task = get_object_or_404(Task_list, id=id)
    task.delete()
    projects = list(Task_list.objects.values())
    return render(request, 'task.html', {
        'projects' : projects
    })

def update_task(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task_list, id = task_id)

        return render(request, 'update_task.html',{
            'form': UpdateTask(instance= task)
        })
    if request.method == "POST":
        print(task_id)
        Task_list.objects.filter(id=task_id).update(name= request.POST['name'], description = request.POST['description'] ,date_end= request.POST['date_end'])
        return redirect("/Tareas")
        # return JsonResponse({"message": f"Tarea {task_id} cambiada"})
    
def change_state_task(request, task_id):
    task = get_object_or_404(Task_list, id=task_id)
    task.completada = not task.completada
    task.save()
    projects = list(Task_list.objects.values())
    return render(request, 'task.html', {
        'projects' : projects
    })
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task_list
import json

@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data_post = json.loads(request.body)

        task = Task_list.objects.create(
                    name=data_post["name"], 
                    description=data_post["description"],
                    date_end = data_post["date_end"]
                )
        
        response_data = {
            "id": task.id,
            "name": task.name,
            "description": task.description
        }

        return JsonResponse(response_data)
    return JsonResponse({"error": "El method es incorrecto"})


@csrf_exempt
def get_all_tasks(request):
    if request.method == "GET":
        tasks = Task_list.objects.all()

        task_list = list(tasks.values())

        return JsonResponse(task_list, safe=False)
    return JsonResponse({"error": "El method es incorrecto"})


@csrf_exempt
def get_task_by_id(request, task_id):
    if request.method == "GET":
        try:
            task = Task_list.objects.get(id=task_id)
        
            print(task)

            response_data = {
                "id": task.id,
                "name": task.name,
                "description": task.description
            }

            return JsonResponse(response_data)
        except:
            return JsonResponse({})

    return JsonResponse({"error": "El method es incorrecto"})

@csrf_exempt
def delete_task(request):
    if request.method == "DELETE":
        try:

            data_post = json.loads(request.body)

            task = Task_list.objects.get(id=data_post["task_id"])
            
            response_data = {
                "id": task.id,
                "name": task.name,
                "description": task.description
            }

            task.delete()

            return JsonResponse({"msg": "Tarea eliminada", "task": response_data})
        except:
            return JsonResponse({"error": "No se encontro la tarea para eliminar"})
    return JsonResponse({"error": "El method es incorrecto"})


@csrf_exempt
def delete_task_by_id(request, task_id):
    if request.method == "DELETE":
        try:

            task = Task_list.objects.get(id=task_id)
            
            response_data = {
                "id": task.id,
                "name": task.name,
                "description": task.description
            }

            task.delete()

            return JsonResponse({"msg": "Tarea eliminada", "task": response_data})
        except:
            return JsonResponse({"error": "No se encontro la tarea para eliminar"})
    return JsonResponse({"error": "El method es incorrecto"})

@csrf_exempt
def udpate_task(request):
    if request.method == "PUT":
        try:
            data_post = json.loads(request.body)
            task = Task_list.objects.get(id=data_post["id"])

            task.name = data_post.get("name", task.name)
            task.description = data_post.get("description", task.description)
            task.date_end = data_post.get("date_end", task.date_end)

            task.save()

            response_data = {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description
                }
            return JsonResponse({"msg": "Tarea editada", "task": response_data})
        except:
            return JsonResponse({"error": "No se encontro la tarea para editar"})
    return JsonResponse({"error": "El method es incorrecto"})

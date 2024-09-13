"""
URL configuration for APP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from task.views import main, task, create_tasks, update_task, delete_tasks, change_state_task
from task import viewsApi
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main,name='main'),
#     path('Tareas', task, name='task' ),
#     path('Crear', create_tasks, name='crear_tasks'),
#     path('Actualizar_Tarea/<int:task_id>', update_task, name= 'Actualizar_Tarea'),
#     path('Eliminar_Tarea/<int:id>', delete_tasks, name='Eliminar_Tarea'),
#     path('Marcar_tarea/<int:task_id>', change_state_task, name='Marcar_tarea')
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_task', viewsApi.create_task, name="create_task"),
    path('api/get_all_tasks', viewsApi.get_all_tasks, name="get_all_tasks"),
    path('api/get_task_by_id/<int:task_id>', viewsApi.get_task_by_id, name="get_task_by_id"),
    path('api/delete_task', viewsApi.delete_task, name="delete_task"),
    path('api/delete_task_by_id/<int:task_id>', viewsApi.delete_task_by_id, name="delete_task_by_id"),
    path('api/udpate_task', viewsApi.udpate_task, name="udpate_task"),
    path('api/get_token_csrf', viewsApi.get_token_csrf, name="get_token_csrf"),
]
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
from task.views import main, task, create_tasks, update_task, delete_tasks, change_state_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main,name='main'),
    path('Tareas', task, name='task' ),
    path('Crear', create_tasks, name='crear_tasks'),
    path('Actualizar_Tarea/<int:task_id>', update_task, name= 'Actualizar_Tarea'),
    path('Eliminar_Tarea/<int:id>', delete_tasks, name='Eliminar_Tarea'),
    path('Marcar_tarea/<int:task_id>', change_state_task, name='Marcar_tarea')
]

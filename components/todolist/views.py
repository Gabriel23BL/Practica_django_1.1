from django.shortcuts import render
from .models import task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def todolist(request):
    db_data = task.objects.all()
    context = {
        'db_data': db_data[::-1],
        'update': None
    }
    
    return render(request, 'todolist/todolist.html', context)

#Agregar tareas
def insert(request):
    try:
        task_subject = request.POST['subject']
        task_description = request.POST['description']
        if task_subject == '' or task_description == '':
            raise ValueError('El texto no puede estar en vacio')
        db_data = task(subject=task_subject, description=task_description)
        db_data.save()
        return HttpResponseRedirect(reverse('todolist'))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect (reverse('todolist'))

#Actualizar tareas
def update(self):
    return HttpResponseRedirect(reverse('todolist'))

def update_form(request, task_id):
    db_data = task.objects.all()
    db_data_only = task.objects.get(pk=task_id)

    context = {
        'db_data': db_data[::-1],
        'update': db_data_only
    }

#Eliminar tareas 
def delete(request, task_id):
    db_data = task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse('todolist'))


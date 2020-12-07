from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .models import task

def home(request):
    todo_items = task.objects.all().order_by("-activate_data")
    # print(todo_items)

    return render(request, 'index.html', {"todo_items": todo_items})

def add_on(request):
    return render(request, 'add_on.html')
def save(request):
    cur_task = request.POST["tasktitle"]
    cur_description = request.POST["description"]
    cur_date = timezone.now()
    task.objects.create(activate_data=cur_date, description = cur_description, task_name = cur_task)
    return HttpResponseRedirect("/")

def cancel(request):
    return HttpResponseRedirect("/")

def update(request, task_id):
    cur_task = task.objects.get(id=task_id)
    cur_title = cur_task.task_name
    cur_description = cur_task.description
    print(cur_title)
    print(cur_description)
    return render(request, 'update.html', {'id': task_id,'cur_title': cur_title, 'cur_description': cur_description})

def delete(request, task_id):
    del_object = task.objects.filter(id=task_id)
    del_object.delete()
    return HttpResponseRedirect("/")

def back(request):
    return HttpResponseRedirect("/")

def edit(request, task_id):
    new_title = request.POST["tasktitle"]
    new_description = request.POST["description"]
    new_data = timezone.now()

    task.objects.filter(id=task_id).update(activate_data=new_data, description = new_description, task_name = new_title)
    return HttpResponseRedirect("/")
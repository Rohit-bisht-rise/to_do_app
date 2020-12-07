from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .models import task

def home(request):
    todo_items = task.objects.all().order_by("-activate_data")
    print(todo_items)
    return render(request, 'index.html', {"todo_items": todo_items})

def add_on(request):
    current_data = timezone.now()
    current_task = request.POST["content"]
    current_obj = task.objects.create(activate_data=current_data, task_name=current_task)
    return HttpResponseRedirect("/")

def delete(request, task_id):
    del_object = task.objects.filter(id=task_id)
    del_object.delete()
    return HttpResponseRedirect("/")


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_on/', views.add_on, name="add_on" ),
    path('delete/<int:task_id>/', views.delete, name="delete")
]
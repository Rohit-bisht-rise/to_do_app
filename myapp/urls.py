from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_on/', views.add_on, name="add_on" ),
    path('delete/<int:task_id>/', views.delete, name="delete"),
    path('add_on/cancel/', views.cancel, name="cancel"),
    path('add_on/save/',views.save, name="save" ),
    path('update/<int:task_id>', views.update, name="update"),
    path('update/back/', views.back, name="back"),
    path('update/edit/<int:task_id>', views.edit, name="edit")
]
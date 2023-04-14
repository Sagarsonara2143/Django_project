from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add-task',views.add_task,name='add-task'),
]

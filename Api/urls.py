from django.urls import path
from . import views
urlpatterns = [
    path("",views.getTodos),
    path("addTodo",views.addTodo),
    path('deleteTodo/<int:pk>',views.deleteTodo),
    path('updateTodo/<int:pk>',views.updateTodo),
    path('getTodo/<int:pk>',views.getTodo)
]

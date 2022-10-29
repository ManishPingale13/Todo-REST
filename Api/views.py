from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ToDoSerializer
from rest_framework import status
from .models import ToDo

# Create your views here.

@api_view(["GET"])
def getTodos(request):
    todos = ToDo.objects.all()
    serilizedTodo = ToDoSerializer(todos,many=True)
    return Response(serilizedTodo.data,status=status.HTTP_200_OK)

    

@api_view(["GET"])
def getTodo(request,pk):
    try:
        todo = ToDo.objects.get(id=pk)
    except ToDo.DoesNotExist:
        return Response("The task you are looking for does not exist!",
            status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response("Something went Wrong",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    serilizedTodo = ToDoSerializer(todo)
    return Response(serilizedTodo.data)


@api_view(["POST"])
def addTodo(request, *args, **kwargs):
    serializedTodo = ToDoSerializer(data= request.data)
    if serializedTodo.is_valid(raise_exception=True): 
        serializedTodo.save()
        return Response(serializedTodo.data,status=status.HTTP_201_CREATED) 
    return Response(serializedTodo.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteTodo(request,pk):
    try:
        todo = ToDo.objects.get(id=pk)        
    except ToDo.DoesNotExist:
        return Response("The task you are trying to delete does not exist",
            status=status.HTTP_404_NOT_FOUND)
    except:
        return Response("Something went wrong!",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    todo.delete()
    return Response("Task Deleted Successfully!")
    

@api_view(["PUT"])
def updateTodo(request,pk):
    try:
        todo = ToDo.objects.get(id=pk)        
    except ToDo.DoesNotExist:
        return Response("The task you are trying to update does not exist",
            status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response("Something went Wrong" ,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializedTodo = ToDoSerializer(instance=todo,data=request.data,partial=True)
    if serializedTodo.is_valid(raise_exception=True):
        serializedTodo.save()
        return Response(serializedTodo.data,status=status.HTTP_200_OK)
    return Response("Data not valid! ",status=status.HTTP_400_BAD_REQUEST)

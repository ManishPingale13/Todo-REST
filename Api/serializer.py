import imp
from pyexpat import model
from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
#    timeStamp=serializers.DateTimeField(format="%d-%m-%Y-%H-%M-%S")
    class Meta():
        model = ToDo
        fields = "__all__"

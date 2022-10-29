from pyexpat import model
from django.db import models

# Create your models here.

class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
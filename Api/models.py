from pyexpat import model
from django.db import models
from datetime import datetime

# Create your models here.

class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    timeStamp = models.DateTimeField(default=datetime.now)
    
'''    def save(self,*args,**kwargs):
        if self.timeStamp is None:
            self.timeStamp =  datetime.datetime.now()
        super().save(*args,**kwargs)
'''

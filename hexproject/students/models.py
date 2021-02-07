from django.db import models
from django.urls import reverse
# Create your models here.


class Student(models.Model):
    fullname = models.CharField(max_length=40)
    age      = models.IntegerField()
    born     = models.CharField(max_length=40)


    def __str__(self):
        return self.fullname

    


    def get_absolute_url(self):
        return reverse("studentview", kwargs={"id": self.id})
         
    
        
    

    
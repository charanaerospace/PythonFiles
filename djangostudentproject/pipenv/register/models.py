from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    mobile = models.IntegerField(max_length=10)
    semester = models.IntegerField(max_length=10)
    
    def __init__(self):
        return self.first_name
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 30)
    course = models.CharField(max_length = 35)
    year = models.IntegerField()
    email = models.EmailField(max_length = 40, default = '')
    
    
class Empathy(models.Model):
    title = models.CharField(max_length = 20)
    location = models.CharField(max_length = 30)
    trainer = models.CharField(max_length = 25)

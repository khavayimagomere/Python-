from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length = 35)
    email = models.EmailField(max_length = 40)
    comments = models.TextField

class Reader(models.Model):
    About = models.TextField
    contact = models.IntegerField 
    
    
    
    
    
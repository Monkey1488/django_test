from ast import keyword
from django.db import models

# Create your models here.
class Point(models.Model):
    title = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    keywords = models.TextField()
    
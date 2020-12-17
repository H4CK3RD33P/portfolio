from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    

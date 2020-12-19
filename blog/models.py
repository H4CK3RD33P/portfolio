from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
        #this method will let Django admin panel to display the name of the object not as
        ##'Blog object (int)' but as the title attibute of the Blog object
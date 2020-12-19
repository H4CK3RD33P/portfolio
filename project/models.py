from django.db import models
#models are the objects that will be put into the database through admin panel

# Create your models here.
class Project(models.Model): #We inherit Model class from model
    title = models.CharField(max_length=200) #CharField class will provide a Java like TextField in the admin panel
    description = models.CharField(max_length=300) #max_length parameter will limit the maximum length of the text entered
    image = models.ImageField(upload_to='images/') #ImageField will let you upload images and will validate it and store it in the specified folder
    url = models.URLField(blank=True) #URLField will let you write URL

    def __str__(self):
        return self.title
        #this method will let Django admin panel to display the name of the object not as
        ##'Project object (int)' but as the title attibute of the project object
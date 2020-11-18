from django.contrib import admin
from .models import Project #I import the Project class from models.py inside project folder
# Register your models here.
admin.site.register(Project) #I register the project class with admin, and now it will show up in the admin panel
from django.shortcuts import render
from .models import Project #importing the Project class from models.py
# Create your views here.
def home(request):
    projects = Project.objects.all() #list of all the project that are created and stored inside the database   
    return render(request,'project/home.html',{'projects':projects }) #passed the list of projects as a dictionary
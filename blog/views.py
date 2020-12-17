from django.shortcuts import render,get_object_or_404 #get_object_or_404() gets the required object and if not found, gives 404 error
from .models import blog
# Create your views here.

def all_blogs(request):
    blogs = blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs': blogs})

def detail(request,blog_id):
    #The first argument is the class blog and second is the primary key of the object
    blog_obj = get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog_obj})
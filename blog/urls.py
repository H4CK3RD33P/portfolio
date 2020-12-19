from django.urls import path
from . import views

app_name = 'blog' #this will set the app name to blogs which will enable all the other apps to use the urls of this app by referring to it with the name. 

urlpatterns = [
    path('',views.all_blogs,name="all_blogs"),
    path('<int:blog_id>/',views.detail,name="detail") #<int:blog_id> means we enter a 'int' object which is reffered as 'blog_id'
]

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.all_blogs,name="all_blogs"),
    path('<int:blog_id>/',views.detail,name="detail") #<int:blog_id> means we enter a 'int' object which is reffered as 'blog_id'
]

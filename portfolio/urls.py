"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static #this function will add media url and root to urlpattern list
from django.conf import settings #importing the settings.py configuration
from project import views #importing the views for project app where the home() exists
from django.urls import include #importing include() using which we can forward the traffic to urls.py of some other app and let it handle using its own views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'), #when user gives the url with '/' at the end, it will pass it to home() in project/views.py
    path('blog/', include('blog.urls')), #when user adds /blog/ to the url, it will be forwarded to blog/urls.py which will then handle the request
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

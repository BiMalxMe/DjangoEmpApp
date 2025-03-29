"""
URL configuration for office_emp_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include


#Yo chai main Project Ko urls.py bhanne wala file ho
#  Yp office_emp_proj chai main company vayeko va emp_app chai yesko euta sector ho

#path localhost:8000/admin vayo bhanee admin panel lai redirect garxa
#include le emp_app bhanew sector ko urls lai pani enlist garxa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp_app.urls')),
]

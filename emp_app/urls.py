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
from . import views


#yesma hamle views.py ma vako function lai evoke garna sakhxau 
# suru ko argument le chai / paxi k vaye kata redirect garne sambhandi
# janakari rakhxa

urlpatterns = [
    path('', views.index, name="index"),
    path('view_all_emp', views.view_all_emp, name="view_all_emp"),#the string youwrite in the name canbe used in href as {% url 'view_all_emp' %}
    path('add_emp', views.add_emp, name="add_emp"),
    path('remove_emp', views.remove_emp, name="remove_emp"),
    path('remove_emp/<int:emp_id>', views.remove_emp, name="remove_emp"),
    path('filter_emp', views.filter_emp, name="filter_emp")
]

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def all_emp(request):
    return render(request,"view_all_emp")

def add_emp(request):
    return render(request,"add_emp")

def remove_emp(request):
    return render(request,"remove_emp")

def filter_emp(request):
    return render(request,"filter_emp")
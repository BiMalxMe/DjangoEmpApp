from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,"index.html")

def view_all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emps':emp
    }
    print(context)
    return render(request,"view_all_emp.html",context)
def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept,
            salary=salary,
            bonus=bonus,
            role_id=role,
            phone=phone,
            hire_date= datetime.now() # Save hire_date
        )
        new_emp.save() 
        return HttpResponse("Employee Added")
    elif request.method == "GET":    
        return render(request,"add_emp.html")
    else:
        return HttpResponse("An Error Occurred")

def remove_emp(request):
    return render(request,"remove_emp.html")

def filter_emp(request):
    return render(request,"filter_emp.html")
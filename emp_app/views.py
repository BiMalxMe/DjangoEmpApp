from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
#hamle Employee matrai import gare hunx kinaki aru ta sabai foreign key ko rupma baseko xa
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")

def view_all_emp(request):
    #YEsle chai Employe ko data lai json format ma rakhxa
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
        #Employee ma naya data lai feri Add garne
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
         departments = Department.objects.all()
         roles = Role.objects.all()
        #  print(departments)
        #  print(roles)   Added Debugging ko lagi
         return render(request, "add_emp.html", {
            "departments": departments,
            "roles": roles
        })
    else:
        return HttpResponse("An Error Occurred")

def remove_emp(request,emp_id):
    if emp_id:
        try:
            emp_to_be_deleted = Employee.objects.get(id=emp_id)
            emp_to_be_deleted.delete()
            return HttpResponse("Emp delted Sucessfully")
        except:
            return HttpResponse("An Error Occurred While Deleting")
    emp = Employee.objects.all()
    context = {
        'emps':emp
    }
    print(context)
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    if request.method=="POST":
        #pathako data lai inherit/Line
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            #Q dina compulary data Query garna
            emps = emps.filter(Q(first_name__icontains =name) | Q(last_name__icontains = name))#icontains le sabi small big case wala dekhauxa
        if dept:
            emps = emps.filter(dept__name =dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            "emps" : emps
        }
        #filter vako data main all show wala ma pathaune
        return render(request,"view_all_emp.html",context)
    elif request.method == "GET":
        return render(request,"filter_emp.html")
    #filter ko criteria xaina bhane tei form wala page lai feri dekhaune
    else:
        return HttpResponse("Something Went Wrong")
    # Yedi kehi pani method deko xaina bhane Reposne dine
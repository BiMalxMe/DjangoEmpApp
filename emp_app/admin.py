from django.contrib import admin
from .models import Employee, Role ,Department

# Register your models here.


#Yesle admin le acess anee modify garna milne models lai list garxa
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)
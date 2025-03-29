from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
#   On delete CASCADE le chai data delte vayo bhane automatically aru data pani delete garx
# In     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#   ROle le yeha foreign key denote gareko xa
#   aba Role ko data delete vayo bhane automatically ROle sanga connect vako employee ko data 
# pani delete hunx
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"

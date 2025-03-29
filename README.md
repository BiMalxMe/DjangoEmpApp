# Django Setup Guide

## **Django Setup Explanation in Roman Nepali**

### **1. Virtual Environment Setup**
Virtual environment (`venv`) banaunda, Django ra aru dependencies haru ekdam ramrai sanga manage garna milcha. Yo le aru projects sanga conflict hunna.

```bash
# Windows ma virtual environment banauna
python -m venv env

# Mac/Linux ma
python3 -m venv env
```

**Activate garna:**
```bash
# Windows (CMD)
env\Scripts\activate

# Windows (PowerShell)
env\Scripts\Activate.ps1

# Mac/Linux
source env/bin/activate
```

Yo vanda pachi **terminal ma (env)** dekhincha, jasko matlab virtual environment chalirako cha.

### **2. Django Install garne**
Django install garna yo command use garne:
```bash
pip install django
```
**Check garna:**
```bash
pip freeze
```
Yo command le `django` install vayo ki nai check garna madad garxa.

### **3. Django Project Start garne**
```bash
django-admin startproject office_emp_proj
```
**office_emp_proj** chai ekdaam **mukhya project** ho, jasma sabai apps haru rakhincha. (Jaile ni company jasto sochne!)

### **4. App banaune**
App chai **company ko ek ek section** jasto ho. Jasari ek company ma HR, Finance, Marketing huncha, tyasari Django ma app bancha.
```bash
cd office_emp_proj
python manage.py startapp emp_app
```
Yo `emp_app` chai employee management ko lagi ho.

### **5. Django Server Run garne**
```bash
python manage.py runserver
```
Yo command le **localhost:8000** ma server start garxa. Website **browser ma kholna milcha!**

### **6. Migrations chalawne (Database set garne)**
Models haru define garepaxi, migration chalawna parcha:
```bash
python manage.py makemigrations
python manage.py migrate
```
**Makemigrations** – Yo chai database ko lagi blueprint banaucha.
**Migrate** – Yo chai database ma actual changes garxa.

### **7. Admin Superuser banaune**
Django ko **admin panel** (Dashboard) access garna superuser banauna parcha.
```bash
python manage.py createsuperuser
```
Yo command le **username, email ra password** magcha. Paxi `http://127.0.0.1:8000/admin/` ma login garna milcha.

### **8. Server feri chalawne**
```bash
python manage.py runserver
```
Paxi `http://127.0.0.1:8000/` visit garera **project check** garna milcha!

### **9. Virtual Environment Deactivate garne**
Kaam sakiyepaxi, venv **off** garna:
```bash
deactivate
```
Esari garera Django project suru garna milcha! 🎯 🚀

Aba kei confusion xa vane sodhna sakxau! 😃

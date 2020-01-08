from django.shortcuts import render
from .models import Employee

# Create your views here.
def employee_index(request):
    all_employee=Employee.objects.all()
    context={
        "employee":all_employee
    }
    return render(request,'employee_index.html',context=context)

def emp_update_form(request):
    context={
        "action":"update"
    }
    return render(request,'update_empolyee_details.html',context=context)

def emp_add_form(request):
    context={
        "action":"add"
    }
    return render(request,'add_employee_details.html',context=context)

from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    
    employee_list=Emp.objects.all()
    context={
        'employee_list':employee_list
    }
    return render(request,'index.html',context)


def add_employee(request):
    if request.method=="POST":
       name=request.POST['name']
       Email_id=request.POST['Email_id']
       Contact_No=request.POST['Contact_No']
       Location=request.POST['Location']
       Image=request.POST['Image']
       employee=Emp(name=name,Email_id=Email_id,Contact_No=Contact_No,Location=Location)
       employee.save()
       messages.info(request,"EMPLOYEE ADDED SUCCESSFULLY")

    else:
        pass


    employee_list=Emp.objects.all()
    context={
        'employee_list':employee_list
    }
    return render(request,'index.html',context)




def delete_employee(request,myid):
    employee=Emp.objects.get(id=myid)
    employee.delete()
    messages.info(request,"Employee Deleted Successfully")
    return redirect(index)



def edit_employee(request,myid):
    sel_employee=Emp.objects.get(id=myid)
    employee_list=Emp.objects.all()
    context={
        'sel_employee':sel_employee,
        'employee_list':employee_list
    }
    return render(request,'index.html',context)




def update_employee(request,myid):
    employee=Emp.objects.get(id=myid)
    employee.name=request.POST["name"]
    employee.Email_id=request.POST["Email_id"]
    employee.Contact_No=request.POST["Contact_No"]
    employee.Location=request.POST["Location"]
    employee.Image=request.POST["Image"]
    employee.save()
    messages.info(request,"Employee Details Updated Successfully")
    return redirect('index')
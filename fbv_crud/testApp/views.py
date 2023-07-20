from django.shortcuts import render,redirect
from testApp.models import Employee
from testApp.forms import EmployeeForm
# Create your views here.
def retrive_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testApp/index.html',{'emp_list':emp_list})


def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/retrive')

def insert_view(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/retrive')
    return render(request,'testApp/insert.html',{'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/retrive')

def update_view(request,id):
    employee=Employee.objects.get(id=id) 
    form=EmployeeForm(instance=employee)
    if request.method == 'POST': 
        form=EmployeeForm(request.POST,instance=employee) 
        if form.is_valid(): 
            form.save() 
        return redirect('/retrive') 
    return render(request,'testApp/update.html',{'form':form}) 

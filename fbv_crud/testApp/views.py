from django.shortcuts import render
from testApp.models import Employee
from testApp.forms import EmployeeForm
# Create your views here.
def retrive_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testApp/index.html',{'emp_list':emp_list})

def insert_view(request):
    form = EmployeeForm()
    return render(request,'testApp/insert.html',{'form':form})
from django.shortcuts import render
from testApp.models import Employee 
# Create your views here.
def retrive_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(esal__gt=15000)
    # emp_list=Employee.objects.filter(ename__contains='John')
    # emp_list=Employee.objects.filter(ename__icontains='john')
    # emp_list=Employee.objects.filter(id__in=[1,3,5])
    # emp_list=Employee.objects.filter(ename__startswith='jo')
    # emp_list=Employee.objects.filter(ename__endswith='O')
    emp_list=Employee.objects.filter(esal__range=[12000,15000])
    print(type(emp_list))
    return render(request,'testApp/index.html',{'emp_list':emp_list})

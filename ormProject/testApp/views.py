from django.shortcuts import render
from testApp.models import Employee 
from django.db.models import Q
from django.db.models import Avg,Count,Min,Max,Sum
# Create your views here.
def retrive_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(esal__gt=15000)
    # emp_list=Employee.objects.filter(ename__contains='John')
    # emp_list=Employee.objects.filter(ename__icontains='john')
    # emp_list=Employee.objects.filter(id__in=[1,3,5])
    # emp_list=Employee.objects.filter(ename__startswith='jo')
    # emp_list=Employee.objects.filter(ename__endswith='O')
    # emp_list=Employee.objects.filter(esal__range=[12000,15000])
    # emp_list=Employee.objects.filter(ename__startswith = 'D') | Employee.objects.filter(esal__gt = 15000)
    # emp_list = Employee.objects.filter(Q (ename__startswith='D')| Q (esal__lt=15000))
    # emp_list = Employee.objects.filter(ename__startswith ='D') & Employee.objects.filter(esal__gt=15000)
    # emp_list=Employee.objects.filter(Q(ename__startswith='D') & Q(esal__lt=15000))
    # emp_list = Employee.objects.filter(ename__startswith='D',esal__gt=17000)
    # emp_list = Employee.objects.exclude(ename__startswith='J')
    # emp_list=Employee.objects.filter(~Q(ename__startswith = 'J'))
    # emp_list=Employee.objects.all().values_list('ename','esal')
    emp_list=Employee.objects.all()
    print(type(emp_list))
    return render(request,'testApp/index.html',{'emp_list':emp_list})
def aggregate_view(request):
    avg1=Employee.objects.all().aggregate((Avg('esal')))
    avg2=Employee.objects.all().aggregate((Max('esal')))
    avg3=Employee.objects.all().aggregate((Min('esal')))
    avg4=Employee.objects.all().aggregate((Sum('esal')))
    avg5=Employee.objects.all().aggregate((Count('esal')))
    # my_dict={'avg1':avg1,}
    return render(request,'testApp/index1.html',{'avg1':avg1['esal__avg'],'avg2':avg2['esal__max'],'avg3':avg3['esal__min'],'avg4':avg4['esal__sum'],'avg5':avg5['esal__count']})

from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def templateView(request):
    dt=datetime.datetime.now()
    name='Kunal'
    rollno=101
    marks=100
    my_dict={'date':dt,'name':name,'rollno':rollno,'marks':marks}
    return render(request,'testapp/index.html',context=my_dict)

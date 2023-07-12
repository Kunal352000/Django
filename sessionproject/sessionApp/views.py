from django.shortcuts import render
from sessionApp.forms import LoginForm
import datetime
# Create your views here.
def home_view(request):
    form=LoginForm()
    return render(request,'sessionApp/index.html',{'form':form}) 

def date_time_view(request):
    name=request.GET['name']
    response = render(request,'sessionApp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response

def result_view(request):
    name=request.COOKIES.get('name')
    date_time = datetime.datetime.now()
    response =render(request,'sessionApp/result.html',{'name':name,'date_time':date_time})
    return response

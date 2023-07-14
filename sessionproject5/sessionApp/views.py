from django.shortcuts import render
from sessionApp.forms import *
# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,'sessionApp/index.html',{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name 
    form=AgeForm()
    return render(request,'sessionApp/age.html',{'form':form,'name':name})

def gf_view(request):
    age=request.GET['age']
    request.session['age']=age 
    name = request.session['name']
    form=GfForm()
    return render(request,'sessionApp/gf.html',{'form':form ,'name':name})

def result_view(request):
    gf=request.GET['gf']
    request.session['gf']=gf 
    # name = request.session['name']
    # age = request.session['age']
    # gf = request.session['gf']
    return render(request,'sessionApp/result.html' )

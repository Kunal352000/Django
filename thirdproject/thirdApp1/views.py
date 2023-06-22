from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def timeInformation(request):
    time=datetime.datetime.now()
    s='<h1>Hello Current Date and Time is:'+str(time)+'</h1>'
    return HttpResponse(s)



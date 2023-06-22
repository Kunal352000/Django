from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def goodMorning(request):
    return HttpResponse('<h1>Hello friend Good morning</h1>')

def goodEvening(request):
    return HttpResponse('<h1>Hello Developers Good Evening</h1>')

def goodAfternoon(request):
    return HttpResponse('<h1> Hello friend Good afternoon</h1>')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetingInformation(request):
    return HttpResponse('<h1>Hello GoodMorning</h1>')

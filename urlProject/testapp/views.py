from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstView(request):
    return HttpResponse('<h1>Response from firstView</h1>')

def secondView(request):
    return HttpResponse('<h1>Response from Second View</h1>')

def thirdView(request):
    return HttpResponse('<h1>Response from third view</h1>')

def fourthView(request):
    return HttpResponse('<h1>Response from fourth view</h1>')

def fifthView(request):
    return HttpResponse('<h1>Response from fifth view</h1>')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    s='<h1>Hello Developers</h1>'
    print(s)
    return HttpResponse(s)

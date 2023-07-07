from django.shortcuts import render
from modelApp import studentForm
from . import *
# from modelApp import studentl
# Create your views here.
def student_view(request):
    form=studentForm()
    if request.method=="POST":
        form=studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'modelApp/index.html',{'form':form})
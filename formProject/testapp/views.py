from django.shortcuts import render
from . import forms
# Create your views here.

def studentInputView(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request,'testapp/index.html',context=my_dict)
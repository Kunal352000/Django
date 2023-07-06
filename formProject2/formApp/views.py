from django.shortcuts import render
from . import forms 
# Create your views here.

def studentInputView(request):
    sent = False
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            print("Form validation")
            print("This my dictionary", form.cleaned_data)
            print("NAME: ",form.cleaned_data['name'])
            print("MARKS: ",form.cleaned_data['marks'])
            sent = True
    form=forms.StudentForm()
    return render(request,'formApp/index.html',{'form':form,'sent':sent})
    
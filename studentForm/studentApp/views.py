from django.shortcuts import render
from studentApp.forms import FeedBackForm
# Create your views here.
def feedbackview(request):
    form=FeedBackForm()
    submitted=False
    if request.method=="POST":
        print("inside post")
        form=FeedBackForm(request.POST)
        print("again inside")
        if form.is_valid():
            print("Form Validation Sucess and printing Information")
            print("My data",form.cleaned_data)
            print("Name: ",form.cleaned_data['name'])
            print("RollNo: ",form.cleaned_data['rollno'])
            print("Email: ",form.cleaned_data['email'])
            print("Feedback: ",form.cleaned_data['feedback'])
            submitted=True
            
    
    return render(request,'studentApp/index.html',{'form':form,'submitted':submitted})
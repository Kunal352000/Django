from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def student_view(request):
    form=StudentForm()
    if request.method=="POST":
        print("My Request",request.POST)
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'modelApp/index.html',{"form":form})
        


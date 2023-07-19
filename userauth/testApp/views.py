from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_page_view(request):
    return render(request,'testApp/child.html')

@login_required
def java_page_view(request):
    return render(request,'testApp/javaexams.html')
    
@login_required  
def python_page_view(request):
    return render(request,'testApp/pythonexams.html')

def logout_view(request):
    return render(request,'testApp/logout.html')
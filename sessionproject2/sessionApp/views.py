from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'sessionApp/home.html')
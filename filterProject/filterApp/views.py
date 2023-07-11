from django.shortcuts import render
from filterApp.models import FilterModel
# Create your views here.
def upper_data_view(request):
    records = FilterModel.objects.all()
    return render(request,'filterApp/index.html',{'records':records})
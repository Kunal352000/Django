from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    my_dict = {'insert_date':date}
    return render(request,'testApp/index.html',context=my_dict)
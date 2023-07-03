from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg="Hello Developers! Very Good"
    h=int(date.strftime('%H'))
    if h<12:
        msg+='Morning!'
    elif h<16:
        msg+='Afternoon'
    elif h<21:
        msg+='Evening'
    else:
        msg+='Night'
    my_dict={'date':date,'msg':msg}
    return render(request,'testapp/index.html',my_dict)

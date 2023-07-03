from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg=None
    h=int(date.strftime('%H'))
    if h<12:
        msg="Hello Coders Good Morning!"
    elif h<16:
        msg="Hello Coders Good afternoon!"
    elif h<21:
        msg="Hello Coders Good Evening!"
    else:
        msg="Hello Coders Good Night!"
    my_dict={'date':date,'msg':msg}
    return render(request,'testApp/index.html',my_dict)
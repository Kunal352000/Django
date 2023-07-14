from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    print("This is my cookies",request.COOKIES)
    count=request.session.get('count',0)
    count+=1
    request.session['count']=count
    print("This is my session",request.session.set_expiry(120))
    request.session.set_expiry(120)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'sessionApp/index.html',{'count':count})
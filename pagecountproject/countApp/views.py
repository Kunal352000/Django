from django.shortcuts import render

# Create your views here.
def count_value(request):
    print("This is my cookies:",request.COOKIES)
    count=int(request.COOKIES.get('count',0))
    count+=1
    response = render(request,'countApp/index.html',{'count':count})
    response.set_cookie('count',count)
    return response
from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'sessionApp/home.html')

def age_view(request):
    print('This is my request',request.COOKIES)
    username = request.GET['name']
    response = render(request,'sessionApp/age.html',{'name':username})
    response.set_cookie('name',username,60) #name of the cookie is name and value of the cookie is username for more understanding check home.html
    return response  # we set the username/name for the future purpose

def gf_view(request):
    print("My gf request: ",request.COOKIES)
    username = request.COOKIES['name']
    age = request.GET['age']
    response = render(request,'sessionApp/gf.html',{'name':username})
    response.set_cookie('age',age,60) # we set the age for the future purpose
    return response

def result_view(request):
    print("My gf request: ",request.COOKIES)
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    gf = request.GET['gf']
    response = render(request,'sessionApp/result.html',{'name':name,'age':age,'gf':gf})
    response.set_cookie('gf',gf)
    return response
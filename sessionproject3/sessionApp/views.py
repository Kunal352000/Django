from django.shortcuts import render
from sessionApp.forms import AddItemForm
# Create your views here.
def index_view(request):
    return render(request,'sessionApp/index.html')

def additem_view(request):
    form=AddItemForm()
    response = render(request,'sessionApp/additems.html',{'form':form})
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemName']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity,120)
    return response

def display_items_view(request):
    return render(request,'sessionApp/displayitems.html')
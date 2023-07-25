from django.shortcuts import render
from testApp.models import Company 
from django.views.generic import ListView,DetailView
# Create your views here.
class CompanyListView(ListView):
    model = Company 
    #default template file: company_list.html
    #default context object NAME : company_list

class CompanyDetailView(DetailView):
    model = Company 


    
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testApp.models import Company
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model=Company
    #default template file --> company_list.html
    #default context object -->company_list

class CompanyDetailView(DetailView):
    model = Company
    #default template file --> company_detail.html
    #default context object --> company

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
    #default template name is company_form.html

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('location','ceo')

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
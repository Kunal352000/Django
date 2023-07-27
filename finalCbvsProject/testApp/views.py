from django.shortcuts import render
from django.views.generic import ListView
from testApp.models import Beer
# Create your views here.
class BeerListView(ListView):
    model = Beer
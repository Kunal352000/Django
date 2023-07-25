from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testApp.models import Book
from django.urls import reverse_lazy
# Create your views here.
class BookListView(ListView):
    model=Book
    
    #default template file name = book_list.html
    #default context object name = book_list
    # context_object_name = 'books'

class BookListView2(ListView):
    model=Book
    template_name = 'testApp/books.html'
    #default template file name = book_list.html
    #default context object name = book_list
    context_object_name = 'books'

class BookDetailView(DetailView):
    model=Book 
    #default template file : book_detail.html
    #default context object : book or object

class BookCreateView(CreateView):
    model=Book
    fields=('title','author','pages','price')

class BookUpdateView(UpdateView):
    model=Book 
    # fields=('pages','price')
    fields = '__all__'
    #The default template is book_form.html

# from django import reverse_lazy
class BookDeleteView(DeleteView):
    model=Book 
    success_url = reverse_lazy('home')
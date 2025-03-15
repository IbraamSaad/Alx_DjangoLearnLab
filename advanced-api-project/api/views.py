from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Create this template
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html' # Create this template
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year'] # Specify the fields to include in the form
    template_name = 'book_form.html' # Create this template
    success_url = reverse_lazy('book_list') # Redirect after successful creation

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year'] # Specify the fields to include in the form
    template_name = 'book_form.html' # Create this template
    success_url = reverse_lazy('book_list') # Redirect after successful update

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html' # Create this template
    success_url = reverse_lazy('book_list')
	


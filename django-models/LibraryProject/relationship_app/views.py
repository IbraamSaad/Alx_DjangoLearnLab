from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import ListView, DetailView

# Create your views here.

def book_list_function(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




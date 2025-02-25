from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView
from .models import Library, Book

# Create your views here.


def book_list_function(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




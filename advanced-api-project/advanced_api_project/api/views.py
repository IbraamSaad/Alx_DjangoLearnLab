from django.shortcuts import render
from rest_framework.generics
from . models import Book, Author
from . serializers import BookSerializer, AuthorSerializer


# Create your views here.

class CustomBookCreateView(generics.CreateAPIView):
# can be any name, ensure to align with your project as this is sample exampls 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomAuthorCreateView(generics.CreateAPIView):
# can be any name, ensure to align with your project as this is sample exampls 
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CustomAuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
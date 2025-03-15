from django.shortcuts import render
from rest_framework import generics
from . models import Author, Books
from . serializers import BookSerializer, AuthorSerializer

# Create your views here.
class CustomAuthorCreateView(generics.CreateAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class CustomAuthorListView(generics.ListAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class CustomBookCreateView(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class CustomBookListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

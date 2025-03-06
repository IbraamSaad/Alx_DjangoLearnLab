from rest_framework.generics.ListAPIView
from rest_framework import viewsets
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(ListAPIView):
	queryset = Book.objects.all()
	modelserializer = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	modelserializer = BookSerializer


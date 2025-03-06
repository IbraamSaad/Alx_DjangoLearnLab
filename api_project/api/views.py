from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(ListAPIView):
	queryset = Book.objects.all()
	modelserializer = BookSerializer

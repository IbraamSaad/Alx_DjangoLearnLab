from rest_framework import serializers # importing serializers module 
from . models import Author, Book


class BookSerializer(serializers.ModelSerializer): # Bookserilazer to converte data to json file
	class meta: # inner class to displaye the converted data
		mdel = Book
		fields = ['title', 'publication_year', 'author']

	def valdiate(self, data): # function to valdiate income error
		if data['publication_year'] > 2025:
			raise serializers.ValidationError('publication_year must be from 2025 to below')


class AuthorSerializer(serializers.ModelSerializer): # Authorserilazer to converte data to json file
	books = BookSerializer(many=True) # nested Serializer
	class meta:
		mdel = Author
		fields = ['name']
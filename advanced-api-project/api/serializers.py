from rest_framework import serializer
from . models import Author, Book


# BookSerializer for conversion data to json file
class BookSerializer(serializers.ModelSerializer):
	class meta:
		model = Book
		fields = '__all__' # all fields

# AuthorSerializer for conversion data to json file
class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer(many=True, read_only=True) # nested serializers for related many objects
	class meta:
		model = Author
		fields = ['name'] # all fileds
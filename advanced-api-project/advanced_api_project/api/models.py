from django.db import models

# Create your models here.

class Author(models.Model): # Author class inherits models to map  Author tables in database
	name = models.CharField(max_length=50) # name attribute to be mapped in database with 50 chars long

	def __str__(self): 
		return self.name # return the name of the Author from the database

class Book(models.Model): # Book class inherits models to map  Book table in database
	title = models.CharField(max_length=100)  # title attribute to be mapped in database with 100 chars long
	publication_year = models.IntegerField()  # publication_year attribute to be mapped in database as an IntegerField
	author = models.ForeignKey(Author, on_delete=models.CASCADE) # author attribrute represent a foreign key for Author class as on to many

	def __str__(self):
		return self.title

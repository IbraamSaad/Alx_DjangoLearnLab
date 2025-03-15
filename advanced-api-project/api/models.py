from django.db import models

# Author model to be mapped in db
class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
# Book model to be mapped in db
class Book(models.Model):
	title = models.CharField(max_length=100)
	publication_date = models.IntegerField()
	# foreign key for one to many
	author = models.ForeignKey(Author, on_delete=models.CASCADE) 

	# valdiate publication year
	def valdiate_pulication_year(self, data):
		year = datetime.now().year
		if data > year:
			raise serializers.valdiationError('unvalid publication_date')
		return data

	def __str__(self):
		return self.title


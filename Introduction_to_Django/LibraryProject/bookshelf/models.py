from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	publication_year = models.IntegerField()

class Filtering(models.Model):
	title_name = models.CharField(max_length=200, blank=True, null=True)
	for name in Book.objects.all():
		if name.title in Book.title:
			title_name.append(name.title)
	
	print(title_name)




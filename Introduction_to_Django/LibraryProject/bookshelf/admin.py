from django.contrib import admin

# admin.ModelAdmin

# Register your models here.
from .models import Book, Filtering
admin.site.register(Book)
# "list_filter", "author", "publication_year"
admin.site.register(Filtering)


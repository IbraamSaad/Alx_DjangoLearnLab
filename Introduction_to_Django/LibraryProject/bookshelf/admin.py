from django.contrib import admin

# Register your models here.
from .models import Book, Filtering
admin.site.register(Book)
admin.site.register(Filtering)


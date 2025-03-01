from django import forms
from .models import Book

class BookForm(ModelForm):
	class meta:
		model = Book
		fields = ['title', 'author', 'publication_date']  
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
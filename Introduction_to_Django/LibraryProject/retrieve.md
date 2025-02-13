for field in book.Book.objects.all():
...     print(field.title)
...     print (field.author)
...     print (field.publication_year)

[comment]: <> ('1984', 'George Orwell', 1949)
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

for field in book.Book.objects.all():
...     print(field.title)
...     print (field.author)
...     print (field.publication_year)

book=Book.objects.filter(author="Nineteen Eighty-Four")

book = Book.objects.all.delte()


Book.ojects.all().delete()


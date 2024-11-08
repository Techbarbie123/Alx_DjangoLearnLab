# Delete Operation

Command:
```python
from bookshelf.models import Book  # Import the Book model

# Retrieve and delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by checking for all Book objects
Book.objects.all()


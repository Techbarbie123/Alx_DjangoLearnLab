### Registering the Book Model with the Django Admin

#### Code:
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)

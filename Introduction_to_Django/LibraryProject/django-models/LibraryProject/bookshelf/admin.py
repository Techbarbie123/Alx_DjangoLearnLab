from django.contrib import admin
from .models import Book

# Define custom admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for the 'author' and 'publication_year' fields
    list_filter = ('author', 'publication_year')

    # Add search functionality for the 'title' and 'author' fields
    search_fields = ('title', 'author')

# Register the Book model with custom admin configurations
admin.site.register(Book, BookAdmin)

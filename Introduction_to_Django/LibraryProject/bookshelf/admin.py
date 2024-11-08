from django.contrib import admin
from .models import Book

# Custom admin configuration for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    list_filter = ('author', 'publication_year')            # Add filters for easy filtering
    search_fields = ('title', 'author')                     # Enable search by title and author

# Register Book model with custom admin configurations
admin.site.register(Book, BookAdmin)


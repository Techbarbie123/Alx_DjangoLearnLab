# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(f"Title: {book.title}")

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Book Title: {book.title}")

# 3. Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian: {librarian.name}")

# Example usage
if __name__ == "__main__":
    # You can replace these calls with actual library and author names from your database
    get_books_by_author("George Orwell")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")

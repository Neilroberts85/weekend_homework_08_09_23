from models.book import Book

book1 = Book("Superworm", "Julia Donaldson", "Kids", False)
book2 = Book("JavaScript Patterns", "Stoyan Stefanov", "Computer Programming", True)
book3 = Book("The Gardeners Year", "Alan Titchmarsh", "Gardening", False)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_to_delete):
    for book in books:
        if book.title == book_to_delete:
            books.remove(book)
            break


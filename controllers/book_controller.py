from flask import Blueprint, render_template, redirect, request
from models.book_list import books, add_new_book, delete_book
from models.book import Book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def index():
    return render_template("index.jinja", title= "My Books", books=books)

@book_blueprint.route('/books/<index>')
def show(index):
  chosen_book = books[int(index)]
  
  return render_template('book.html', book=chosen_book)

@book_blueprint.route('/books', methods=['POST'])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = request.form["checked_out"] == "true"
    new_book = Book(title, author, genre, checked_out)
    add_new_book(new_book)
    return redirect ("/books")



@book_blueprint.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')

from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_book import Book
from flask_app.models.model_favorite import Favorite
from flask_app.models.model_author import Author


# CREATE
@app.route('/add_book', methods=['POST'])
def create_book():
    data={
        **request.form
    }
    Book.create(data)
    return redirect('/books')


# READ
@app.route('/books')
def display_all_books():
    all_books = Book.get_all();
    return render_template("all_books.html", all_books=all_books)

@app.route('/books/<int:book_id>')
def display_one_book(book_id):
    book = Book.get_one(book_id)[0]
    favorited_by = Favorite.get_favorited_by(book_id)
    authors_can_favorite = Favorite.get_unfavorited_author_by_book(book_id)
    return render_template("one_book.html", book=book, favorited_by=favorited_by, authors_can_favorite=authors_can_favorite)
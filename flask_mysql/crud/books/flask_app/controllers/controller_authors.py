from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_author import Author
from flask_app.models.model_favorite import Favorite
from flask_app.models.model_book import Book


# CREATE
@app.route('/add_author', methods=['POST'])
def create_author():
    data={
        **request.form
    }
    Author.create(data)
    return redirect('/authors')


# READ
@app.route('/authors')
def display_all_authors():
    all_authors = Author.get_all()
    return render_template("all_authors.html", all_authors=all_authors)

@app.route('/authors/<int:author_id>')
def display_one_author(author_id):
    author = Author.get_one(author_id)[0]
    favorites = Favorite.get_favorite_books(author_id)
    all_books = Book.get_all()
    return render_template("one_author.html", author=author, favorites=favorites, all_books=all_books)
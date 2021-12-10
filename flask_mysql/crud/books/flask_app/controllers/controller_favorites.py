from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_favorite import Favorite


@app.route('/add_favorite/books', methods=['POST'])
def create_from_books():
    data={
        **request.form
    }
    Favorite.create(data)
    return redirect('/books')

@app.route('/add_favorite/authors', methods=['POST'])
def create_from_authors():
    data={
        **request.form
    }
    Favorite.create(data)
    return redirect('/authors')
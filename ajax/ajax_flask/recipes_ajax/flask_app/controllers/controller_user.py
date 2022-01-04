from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify, get_flashed_messages

from flask_bcrypt import Bcrypt

from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_like import Like

bcrypt = Bcrypt(app)

@app.route('/users/logout')
def users_logout():
    del session['uuid']
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def users_login():
    data = {
        **request.form
    }
    if not User.validate_login(data):
        messages = get_flashed_messages(with_categories=True)
        session.pop('_flashes', None)
        if messages:
            return jsonify(messages)
    
    user_in_db = User.get_user_by_email(data)

    if not user_in_db:
        return jsonify([['err_login', 'Invalid Email/Password']])
    
    if not bcrypt.check_password_hash(user_in_db.password, data['password']):
        return jsonify([['err_login', 'Invalid Email/Password']])
    
    session['uuid'] = user_in_db.id
    return jsonify(redirect="/users/show")

@app.route('/users/new')
def users_new():
    return render_template("users_new.html")

@app.route('/users/create', methods=['POST'])
def users_create():
    if not User.validate_registration(request.form):
        messages = get_flashed_messages(with_categories=True)
        session.pop('_flashes', None)
        if messages:
            return jsonify(messages)
    
    password_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        "password": password_hash
    }

    session['uuid'] = User.create(data)
    return jsonify(redirect="/users/show")

@app.route('/users/show')
def users_show():
    if not "uuid" in session:
        return redirect('/')
    user = User.get_one({"id":session['uuid']})
    all_recipes = Recipe.get_all()
    all_likes = Like.get_all_likes_by_user({"user_id":session['uuid']})
    return render_template("users_show.html", user=user, all_recipes=all_recipes, all_likes=all_likes)


# @app.route('/users/<int:id>/edit')
# def users_edit(id):
#     return redirect('/')

# @app.route('/users/update', methods=['POST'])
# def users_update():
#     return redirect('/')

# @app.route('/users/delete')
# def users_delete():
#     return redirect('/')
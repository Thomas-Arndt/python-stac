from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

# CREATE
@app.route('/users/new')
def index():
    return render_template('index.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    print(request.form)
    data={
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    User.create(data)
    return redirect('/users')

# READ
@app.route('/users')
def users():
    users=User.get_all()
    return render_template("users.html", all_users=users)

@app.route('/users/<user_id>')
def display_user(user_id):
    user = User.get_one(user_id)[0]
    return render_template("display_user.html", user=user)

# UPDATE
@app.route('/users/<user_id>/edit')
def edit_user_page(user_id):
    user=User.get_one(user_id)[0]
    return render_template("edit_user.html", user=user)

@app.route('/edit_user', methods=["POST"])
def edit_user():
    data={
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "user_id": request.form['user_id']
    }
    User.edit(data)
    return redirect("/users/"+request.form['user_id'])


# DELETE
@app.route('/users/<user_id>/delete')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/users')
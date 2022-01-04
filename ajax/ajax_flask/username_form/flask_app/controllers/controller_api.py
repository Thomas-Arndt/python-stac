from flask_app import app
from flask import render_template, jsonify, redirect, session, request, flash

from flask_app.models.model_user import User

@app.route('/api/users/new')
def api_users_new():
    return render_template("api/users_new.html")

@app.route('/api/users/create', methods=['POST'])
def api_users_create():
    print(request.form)
    new_user=User.create(request.form)
    return jsonify(user_id=new_user)

@app.route('/api/users/get_all')
def api_users_get_all():
    all_users=User.api_get_all()
    return jsonify(all_users)

@app.route('/api/users/<int:id>/edit')
def api_users_edit(id):
    return render_template("api/users_edit.html")

@app.route('/api/users/<int:id>/update', methods=['POST'])
def api_users_update(id):
    return redirect('/')

@app.route('/api/users/<int:id>/delete')
def api_users_delete(id):
    return redirect('/')
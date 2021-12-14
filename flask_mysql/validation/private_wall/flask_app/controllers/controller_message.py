from flask_app import app
from flask import render_template, redirect, session, request, flash

from flask_app.models.model_message import Message

@app.route('/messages/new')
def messages_new():
    return render_template("messages_new.html")

@app.route('/messages/<int:receiver_id>/create', methods=['POST'])
def messages_create(receiver_id):
    data = {
        **request.form,
        "receiver_id": receiver_id,
        "sender_id": session['uuid']
    }
    Message.create(data)
    return redirect('/users/show')

@app.route('/messages/<int:id>')
def messages_show(id):
    return render_template("messages_show.html")

@app.route('/messages/<int:id>/edit')
def messages_edit(id):
    return render_template("messages_edit.html")

@app.route('/messages/<int:id>/update', methods=['POST'])
def messages_update(id):
    return redirect('/')

@app.route('/messages/<int:id>/delete')
def messages_delete(id):
    Message.delete_one({"id":id})
    return redirect('/users/show')
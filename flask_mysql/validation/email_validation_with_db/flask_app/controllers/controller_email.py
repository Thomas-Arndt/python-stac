from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.model_email import Email

@app.route('/emails/new')
def emails_new():
    return render_template("emails_new.html")

@app.route('/emails/create', methods=['POST'])
def emails_create():
    if not Email.validate_email(request.form):
        return redirect ('/emails/new')
    
    session['uuid'] = Email.create(request.form)
    return redirect('/emails/show')

@app.route('/emails/show')
def emails_show():
    all_emails = Email.get_all()
    user_email = ""
    if 'uuid' in session:
        user_email = Email.get_one({"id": session['uuid']})
    return render_template("emails_show.html", all_emails=all_emails, user_email=user_email)

@app.route('/emails/<int:id>/edit')
def emails_edit(id):
    return render_template("emails_edit.html")

@app.route('/emails/<int:id>/update', methods=['POST'])
def emails_update(id):
    return redirect('/')

@app.route('/emails/<int:id>/delete')
def emails_delete(id):
    Email.delete_one({"id":id})
    if not Email.get_all():
        return redirect('/emails/new')
        
    return redirect('/emails/show')
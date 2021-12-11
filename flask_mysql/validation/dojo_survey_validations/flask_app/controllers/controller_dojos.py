from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.model_dojo import Dojo

@app.route('/dojos/new')
def dojos_new():
    return render_template("dojos_new.html")

@app.route('/dojos/create', methods=['POST'])
def dojos_create():
    if not Dojo.validate(request.form):
        return redirect('/')
    
    new_user_id=Dojo.create(request.form)
    return redirect('/dojos/'+str(new_user_id))

@app.route('/dojos/<int:id>')
def dojos_show(id):
    data=Dojo.get_one({"id":id})
    return render_template("dojos_show.html", data=data)

@app.route('/dojos/<int:id>/edit')
def dojos_edit(id):
    return render_template("dojos_edit.html")

@app.route('/dojos/<int:id>/update', methods=['POST'])
def dojos_update(id):
    return redirect('/')

@app.route('/dojos/<int:id>/delete')
def dojos_delete(id):
    return redirect('/')
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja


# CREATE
@app.route('/dojos/create', methods=['post'])
def dojo_create():
    data={
        "name": request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

# READ
@app.route('/dojos')
def display_all_dojos():
    dojos=Dojo.get_all_dojos()
    return render_template("dojos.html", all_dojos=dojos)

@app.route('/dojos/<dojo_id>')
def display_one_dojo(dojo_id):
    dojo=Dojo.get_one_dojo(dojo_id)
    ninjas=Ninja.get_all_ninjas(dojo_id)
    return render_template("dojo_show.html", dojo=dojo, all_ninjas=ninjas)


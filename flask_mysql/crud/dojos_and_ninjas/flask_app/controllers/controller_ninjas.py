from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja



# CREATE
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print(request.form)
    data={
        "fname": request.form['first_name'],
        "lname": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }

    Ninja.create_ninja(data)
    return redirect("/dojos/"+request.form['dojo_id'])

# READ
@app.route('/ninjas')
def display_ninja_registration():
    dojos=Dojo.get_all_dojos()
    return render_template("ninja.html", all_dojos=dojos)
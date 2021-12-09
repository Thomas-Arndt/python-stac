from flask import Flask, render_template, redirect, request
from users import Users

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def users():
    users=Users.get_all()
    return render_template("users.html", all_users=users)

@app.route('/create_user', methods=["POST"])
def create_user():
    print(request.form)
    data={
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    Users.create(data)
    return redirect('/display')

while __name__=="__main__":
    app.run(debug=True)
    
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.pop('count')
    session.pop('visits')
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    session['visits'] -= 1
    return redirect('/')

@app.route('/user_increment', methods=['POST'])
def user_increment():
    increment = request.form['user_input']
    print(increment)
    session['count'] += int(increment)-1
    session['visits'] -= 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
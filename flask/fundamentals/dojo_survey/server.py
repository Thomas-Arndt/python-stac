from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # print(request.form)
    session['name']=request.form['name']
    session['email']=request.form['email']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['gender']=request.form['gender']
    session['comments']=request.form['comments']
    signup=request.form['newsletter']
    if signup == "on":
        session['signup']="Yes, send me special offers!"
    else:
        session['signup']="No, don't send me any offers."
    return redirect('/result')

@app.route('/result')
def display_results():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)
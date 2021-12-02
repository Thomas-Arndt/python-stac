from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "You've got a brand new pair of rollerskates, I've got a brand new key"

@app.route('/')
def root():
    session['rand_num'] = random.randint(1, 100)
    session['guess_count'] = 0
    print(session['rand_num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    response_correct = "Take a guess!"
    response_wrong = ""
    guess=request.form['user_input']
    session['guess_count'] +=1
    if int(guess) > session['rand_num']:
        response_wrong = "Your guess was too high..."
        return render_template('guess.html', response_wrong=response_wrong, response_correct=response_correct)
    elif int(guess) < session['rand_num']:
        response_wrong = "Your guess was too low..."
        return render_template('guess.html', response_wrong=response_wrong, response_correct=response_correct)
    else:
        response_correct = f"{session['rand_num']} was the number!"
        response_display = "none"
        response_color = "green"
        return render_template('correct.html', response_wrong=response_wrong, response_correct=response_correct)

if __name__=="__main__":
    app.run(debug=True)
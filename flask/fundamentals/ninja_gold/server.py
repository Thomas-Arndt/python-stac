from flask import Flask, render_template, redirect, request, session
import random

app= Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def root():
    if 'activity' not in session or 'gold' not in session:
        return redirect('/reset')
    else:
        return render_template('index.html')

@app.route('/process_money/<low>/<high>/<prop>', methods=["POST"])
def process_money(low, high,prop):
    random_gold=random.randint(int(low), int(high))
    session['gold']+=random_gold
    if random_gold>=0:
        session['activity']+="<li class='green-text'>You earned "+str(random_gold)+" from the "+prop+".</li>"
    else:
        session['activity']+="<li class='red-text'>You lost "+str(random_gold)+" from the "+prop+".</li>"
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold']=0
    session['activity']=""
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
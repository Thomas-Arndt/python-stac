from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', x=3, color="dodgerblue")

@app.route('/play/<x>')
def box_repeat(x):
    return render_template('index.html', x=int(x), color="dodgerblue")

@app.route('/play/<x>/<color>')
def number_and_color(x, color):
    return render_template('index.html', x=int(x), color=color)


if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('index.html', x=8, y=8, color_one="red", color_two="black")

@app.route('/<y>')
def four_by_eight(y):
    return render_template('index.html', x=8, y=int(y), color_one="red", color_two="black")

@app.route('/<x>/<y>')
def x_by_y(x, y):
    return render_template('index.html', x=int(x), y=int(y), color_one="red", color_two="black")

@app.route('/<x>/<y>/<color_one>/<color_two>')
def x_by_y_choose_color(x, y, color_one, color_two):
    return render_template('index.html', x=int(x), y=int(y), color_one=color_one, color_two=color_two)


if __name__=="__main__":
    app.run(debug=True)
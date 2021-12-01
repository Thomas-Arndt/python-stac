from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hello(name):
    return f"Hello, {name}!"

@app.route('/repeat/<number>/<word>')
def repeat_word(number, word):
    return_string = ""
    for idx in range(int(number)):
        return_string += str(word) + " "
    return return_string

if __name__ == "__main__":
    app.run(debug=True)
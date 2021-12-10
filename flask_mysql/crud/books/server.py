from flask_app import app
from flask_app.controllers import controller_authors
from flask_app.controllers import controller_books
from flask_app.controllers import controller_favorites

while __name__=="__main__":
    app.run(debug=True)
from flask_app import app
from flask_app.controllers import controller_routes
from flask_app.controllers import controller_user

while __name__=="__main__":
    app.run(debug=True)
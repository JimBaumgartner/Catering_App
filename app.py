from flask import Flask
from Models import db
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from Services import bcrypt
from Models import SQLAlchemy
from Controllers import jwt , auth_blueprint, event_controller



app = Flask(__name__)
app.config.from_object('config.Development')
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)


app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(event_controller, url_prefix="/blog")

if __name__ == "__main__":
  app.run(debug = True)



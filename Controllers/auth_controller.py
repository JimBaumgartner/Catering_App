from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from Models.client import create_user
from flask_login import flask_logout

auth_blueprint = Blueprint('auth_api', __name__)  #createing namespace for he auth 
# blueprint to be hit brining in that namnespace,  ie setting a name for it,  __name__ 
#  is something blueprint requires


@app.route("/register", methods=['POST'])
def auth_register():  #this function is to create a user.
    body = request.json
    bcrypt.generate_password_hash(body['password']).decode('utf-8'),
    message = create_user(
        body['email'],
        body['password'],
        body['f_name','l_name'],
    )
        
    return {
        'message': message
    }


@auth_blueprint.route('/register', methods=['POST'])
def register():
    body = request.json
    message = create_user(
    body['email'],
    bcrypt.generate_password_hash(body['password']).decode('utf-8'),
    body['f_name'],
    body['l_name'])
    # print(body['email'], body['password'], body['f_name'], body['l_name'])

    return {
        'message': message
    }



@app.route("/login", methods=['POST'])
def auth_login():  #this function is to allow user to login and will return authintication token
  body = request.json # the body of the request
  print(body)
  to_check = Client.query.filter_by(email=body['email']).first() 
  access_token = create_access_token(to_check.id) # 
  return session_token




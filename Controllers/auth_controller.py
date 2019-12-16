from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from Models.client import create_user
from Services import bcrypt
from Services.client_services import create_user

auth_blueprint = Blueprint('auth_api', __name__)  #createing namespace for he auth 
# blueprint to be hit brining in that namnespace,  ie setting a name for it,  __name__ 
#  is something blueprint requires

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



@auth_blueprint.route("/login", methods=['POST'])
def login():
    body = request.json  # grabbing the data from the body of the request in a json format

    to_check = Client.query.filter_by(email=body['email']).first() # looking in user.py (in models) query by email, then filtering by email grabing the first one
    if bcrypt.check_password_hash(to_check.password, body['password']): #using bcryct model check_password_hash (takes in plain text and hashed password,runs a check to see if they match) then creates JWT Token and return it
        access_token = create_access_token(to_check.id) #if the email and passwords match 
        #                                                generate token with user id
        return {
            'message': 'Hey, you logged in', #if everything checks out then it will return message and token
            'token': access_token
        }
    else:
        return {
            'message': 'Incorrect password' #if does not check out then will just say message: incorrect password
        }




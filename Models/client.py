from datetime import datetime  # importing library called datetime
from . import db  #importing from . (one level up) Models/__init__ where we renamed sqlAlchemy to db
from Controllers.client_controllers import create_user
from marshmallow import Schema, fields  #importing library

class Client(db.Model):  # this class will be used to create users 
    __tablename__ = 'client'  #setting __tablename__ to 'CLIENTS'
    email = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)


def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        self.date_created = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

def save(self):  #createing a function to save the user created
        db.session.add(self)  # this one adds the user to the database (sqlAlchemy)
        db.session.commit()
        return 'User succesfully created'


@staticmethod
def get_all_clients():
  return client.query.all()
    
@staticmethod
def get_one_clients(post_id):
  return Event.query.filter_by(id=post_id).first()


class ClientSchema(Schema):
  id = fields.Int(dump_only=True)
  user_id = fields.Str(required=True)
  date_created = fields.DateTime(dump_only=True)
  last_modified= fields.DateTime(dump_only=True)
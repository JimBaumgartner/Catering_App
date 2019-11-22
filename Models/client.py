import datetime  # importing library called datetime
from . import db  #importing from . (one level up) Models/__init__ where we renamed sqlAlchemy to db
from Controllers.client_controllers import create_user
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
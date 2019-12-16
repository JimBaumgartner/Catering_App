from . import db  #importing from . (one level up) Models/__init__ where we renamed sqlAlchemy to db
from datetime import datetime  #importing library
from marshmallow import Schema, fields  #importing library

class Event(db.Model):
  __tablename__ = 'events'  #defined table name
  id = db.Column(db.Integer, primary_key=True)
  title= db.Column(db.String(30), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  date_created = db.Column(db.DateTime)
  last_modified= db.Column(db.DateTime)



def __init__(self, title,client_id,date_created,last_modified):
  self.title = title
  self.client_id = client_id
  self.date_created = date_created
  self.last_modified = last_modified

def save(self):
  db.session.add(self)
  db.session.commit()

def delete(self):
  db.session.delete(self)
  db.session.commit()

def update(self, old, data):
  for key, item in data.items():
      setattr(old, key, item)
  self.modified_at = datetime.utcnow()
  db.session.commit()
  return old

@staticmethod
def get_all_events():
  return Event.query.all()
    
@staticmethod
def get_one_event(post_id):
  return Event.query.filter_by(id=post_id).first()

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Str(required=True)
    date_created = fields.DateTime(dump_only=True)
    last_modified = fields.DateTime(dump_only=True)
from flask import Blueprint, request
from flask_jwt_extended import create_access_token



@app.route("/new", methods=['POST'])
def event_new():
  return "event_new route hit"


@app.route("/all", methods=['GET'])
def event_all():
  return "a list of all events list hit"

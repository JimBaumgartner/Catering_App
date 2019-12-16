from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity

from Services.event_services import new_event, edit_event, delete_event
from Models.event import Event


event_blueprint = Blueprint('event_api', __name__)

@event_blueprint.route('/new', methods=['POST'])
@jwt_required
def create_event():
    user = get_jwt_identity()
    data = request.json
    return new_event(data, user)


@event_blueprint.route('/all', methods=['GET'])
@jwt_required
def all_event():
    x = fetch_events()
    return custom_response(x, 200)



@event_blueprint.route('/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def single_event(post_id):
    if request.method == 'GET':
        event = fetch_one_event(post_id)
        if event:
            return custom_response(event, 200)

    elif request.method == 'PUT':
        data = request.json
        user = get_jwt_identity()
        event = fetch_one_event(post_id)
        if str(user) == event['user_id']:
            return custom_response(edit_event(post_id, data), 200)

    elif request.method == 'DELETE':
        user = get_jwt_identity()
        event = fetch_one_event(post_id)
        if str(user) == event['user_id']:
            return custom_response(delete_event(event), 204)
    else:
        return 'Method not allowed', 405
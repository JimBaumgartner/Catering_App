from Models.event import Event, EventSchema
from datetime import datetime

event_schema = EventSchema()

def new_event(data, user):
    new_post = Event(
        title=data['title'],
        content=data['content'],
        user_id=user,
        date_created=datetime.utcnow(),
        last_modified=datetime.utcnow()
    )
    try:
        new_post.save()
        message = {
            'Message': f'Event was saved successfully'
        }
        return message, 200
    except Exception as e:
        return str(e), 400

def edit_event(post_id, data):
    x = Event.get_one_event(post_id)
    updated = x.update(x, data)
    new_event = event_schema.dump(updated)
    return new_event

def delete_event(event):
    x = Event.get_one_event(event['id'])
    x.delete()
    return 'Deleted'



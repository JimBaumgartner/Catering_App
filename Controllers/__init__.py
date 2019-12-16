from flask_jwt_extended import JWTManager
from Controllers.auth_controller import auth_blueprint
from Controllers.event_controllers import event_controller

jwt = JWTManager()
from flask_jwt_extended import JWTManager
from .auth_controller import auth_blueprint
from .blog_controller import blog_controller

jwt = JWTManager()
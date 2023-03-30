import os
from flask import Flask
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "some secret key"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
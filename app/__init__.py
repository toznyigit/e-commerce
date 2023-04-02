from flask import Flask
from flask_login import LoginManager
from .auth_model import *
from .database_connector import UserDB

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "some secret key"

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(username):
        userdb = UserDB()
        user = userdb.read(name=username)['type'] if userdb.read(name=username) else None
        log_user = User(DBUser(username, user))
        return log_user

    return app
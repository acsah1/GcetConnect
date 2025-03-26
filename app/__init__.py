from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import logging
from logging import FileHandler
from logging import Formatter


# Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
#migrate = Migrate()

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/gcetconnectdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if not app.debug:
        file_handler = FileHandler('error.log')
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    file_handler = None  
    app.logger.addHandler(file_handler)
    
    # Initialize extensions
    db.init_app(app)
    #migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Register blueprints
    from app.authservice import auth_bp
    from app.main import main_bp
    from app.profileservice import profile_bp
    from app.postservice import postservice_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(postservice_bp, url_prefix='/post')
    
    return app

# Set up the user_loader function after app and db are initialized
from app.authservice.models import User  # Import here to avoid circular import
from app.profileservice.models import Profile
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
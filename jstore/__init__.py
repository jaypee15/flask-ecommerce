
from flask import Flask

from config import Config
from jstore.extensions import db
from jstore.extensions import login_manager
from jstore.extensions import bcrypt


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    

    # Initialize Flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
   
   

    # Register blueprints 
    from . import market
    from . import auth
    app.register_blueprint(market.bp)
    app.add_url_rule('/', endpoint='index')
    app.register_blueprint(auth.bp)
    

    return app


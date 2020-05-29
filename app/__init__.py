# Import flask and template operators
from flask import Flask, render_template
from flask_assets import Environment, Bundle

from flask import got_request_exception
from .components import routeHandler
from .extAPI import ExtendedAPI
from .routes import ROUTING

# Define the WSGI application object
app = Flask(__name__)

# Define Assets
assets = Environment(app)
assets.url = app.static_url_path
assets.url = app.static_url_path
assets.directory = app.static_folder

# Define the REST API
api = ExtendedAPI(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
#db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not Found', 'code': '404'}

# Import a module / component using its blueprint handler variable (mod_auth)
#from app.mod_auth.controllers import mod_auth as auth_module

routeHandler.ROUTING = ROUTING
# Register blueprint(s)
api.add_resource(routeHandler, '/api/<route>')


@app.route('/')
def innit():
    return {'hello': 'world'}
# app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()

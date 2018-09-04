import os

from flask import Flask
from flask_socketio import SocketIO

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    return app

def create_socketio(app):
    socketio = SocketIO(app)
    return socketio
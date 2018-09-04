import os

from flask import Flask
from flask_socketio import SocketIO
from .db import _init_db

def create_app(config_name=None):
    _init_db()
    app = Flask(__name__)
    return app

def create_socketio(app):
    socketio = SocketIO(app)
    return socketio

import os

from flask import Flask
from flask_socketio import SocketIO

from .db import _init_db
from .api import api_bp, ChatSocket

def create_app(config_name=None):
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    _init_db()
    return app

def create_socketio(app):
    socketio = SocketIO(app)
    socketio.on_namespace(ChatSocket('/message/socket'))
    return socketio

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from .db import __init_db
from .api import setupApi


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app=app)
    app = __init_db(app)
    socketio = SocketIO(app)
    setupApi(app, socketio)
    return app, socketio

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from .db import __init_db
from .api import api_bp, MessageSocket


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app=app)
    app = __init_db(app)
    app.register_blueprint(api_bp)
    return app


def create_socketio(app):
    socketio = SocketIO(app)
    socketio.on_namespace(MessageSocket('/message/socket'))
    return socketio

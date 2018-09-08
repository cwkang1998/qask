from flask import Blueprint, jsonify
from flask.views import MethodView
from flask_socketio import emit, Namespace

from .db import mongo
import bson

api_bp = Blueprint('api', __name__, url_prefix='/')

class UserView(MethodView):
    def get(self):
        cur = mongo.db.user.find({})
        users = []
        for doc in cur:
            users.append(doc)
        cur.close()
        return jsonify(users)

    def post(self):
        pass

class RoomView(MethodView):

    def get(self, room_uid):
        pass

    def post(self):
        pass

class MessageSocket(Namespace):

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_message(self):
        pass

    def on_like(self):
        pass
    
    def on_dismiss(self):
        pass

api_bp.add_url_rule('/user', view_func=UserView.as_view('user'))
api_bp.add_url_rule('/room', view_func=RoomView.as_view('room'))
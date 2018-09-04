from flask import Blueprint, jsonify
from flask.views import MethodView
from .db import create_session
from flask_socketio import emit, Namespace

bp = Blueprint('', __name__, url_prefix='/')


class RoomView(MethodView):

    def get(self, room_uid):
        session = create_session()
        data = session.execute(
            "select * from room where room_uid = ?", room_uid)
        if len(data) <= 1:
            return jsonify(data)

    def post(self):
        pass


class UserView(MethodView):
    def get(self):
        pass

    def post(self):
        pass


class ChatSocket(Namespace):
    pass

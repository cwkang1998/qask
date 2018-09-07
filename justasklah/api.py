from flask import Blueprint, jsonify
from flask.views import MethodView
from flask_socketio import emit, Namespace

from .models import *

api_bp = Blueprint('api', __name__, url_prefix='/')


class RoomView(MethodView):

    def get(self, room_uid):
        pass

    def post(self):
        pass


class UserView(MethodView):
    def get(self):
        queryset = User.objects.all()
        pass

    def post(self):
        pass


class MessageView(MethodView):
    def get(self):
        pass

    def post(self):
        pass


class MessageSocket(Namespace):

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

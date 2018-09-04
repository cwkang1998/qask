from flask import Blueprint
from flask.views import MethodView
from flask_socketio import emit, Namespace

bp = Blueprint('', __name__, url_prefix='/')

class RoomView(MethodView):
    def get(self):
        pass
    
    def post(self):
        pass

class UserView(MethodView):
    def get(self):
        pass
    
    def post(self):
        pass
        
class ChatSocket(Namespace):
    pass



from app import create_app, create_socketio
import os


class Config(object):
    DEBUG = TESTING = os.environ.get("ENV") == "development"
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
    MONGO_URI = os.environ.get("DB")


app = create_app(Config)
socketio = create_socketio(app)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')

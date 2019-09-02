from justasklah import create_app, create_socketio
from config import CURRENT_CONFIG
app = create_app(CURRENT_CONFIG)
socketio = create_socketio(app)

if __name__ == '__main__':
    socketio.run(app)
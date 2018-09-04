from justasklah import create_app, create_socketio
from config import DevelopmentConfig, ProductionConfig
app = create_app()
socketio = create_socketio(app)

if __name__ == '__main__':
    socketio.run(app)
    
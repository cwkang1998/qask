import os
from app import create_app, create_socketio

PORT = os.environ.get("PORT", "5000")
TEST = os.environ.get("TEST", False)


class Config:
    DEBUG: bool = os.environ.get("ENV") == "development"
    SECRET_KEY = os.environ.get("SECRET")
    MONGO_URI: str = "mongodb://localhost:27017/qask"


app = create_app(Config)
socketio = create_socketio(app)

if __name__ == "__main__":
    print(f"Running server at {PORT}")
    socketio.run(app, host="0.0.0.0", port=PORT)

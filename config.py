import os

class Config(object):
    DEBUG = True
    SECRET_KEY = "thisisasecretkeyfordevelopment"
    MONGO_URI = "mongodb://localhost:27017/test"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    MONGO_URI = "mongodb://localhost:27017/justasklah"
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

CURRENT_CONFIG = Config
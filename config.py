import os

class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
    MONGO_URI = os.environ.get('DB', default="mongodb://192.168.99.100:27017/justasklah")

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
    MONGO_URI = os.environ.get('DB', default="mongodb://192.168.99.100:27017/justasklah")

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

CURRENT_CONFIG = Config
TESTING_CONFIG = TestingConfig

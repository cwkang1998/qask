import os

class Config(object):
    DATABASE_URI = ''
    SECRET_KEY = 'thisisasecretkeyfordevelopment'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

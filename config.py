import os

class Config(object):
    DEBUG = True
    CASSANDRA_KEYSPACE = 'test'
    SECRET_KEY = 'thisisasecretkeyfordevelopment'

class ProductionConfig(Config):
    CASSANDRA_KEYSPACE = 'justasklah'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

CURRENT_CONFIG = Config
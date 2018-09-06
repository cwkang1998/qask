from cassandra.cqlengine import connection
from cassandra.cqlengine.management import create_keyspace_simple, sync_table
from config import CURRENT_CONFIG
from .models import User, Room, Message


def _init_db():
    connection.setup(['127.0.0.1'], CURRENT_CONFIG.CASSANDRA_KEYSPACE)
    create_keyspace_simple(
        CURRENT_CONFIG.CASSANDRA_KEYSPACE, replication_factor=1)
    _sync_models()


def _sync_models():
    sync_table(User, [CURRENT_CONFIG.CASSANDRA_KEYSPACE,])
    sync_table(Room, [CURRENT_CONFIG.CASSANDRA_KEYSPACE,])
    sync_table(Message, [CURRENT_CONFIG.CASSANDRA_KEYSPACE,])

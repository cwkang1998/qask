from cassandra.cqlengine.models import Model, columns
import uuid
from datetime import datetime


class User(Model):
    id = columns.UUID(primary_key=True, partition_key=True, default=uuid.uuid4)
    session_hash = columns.Text()
    name = columns.Text()
    created_time = columns.DateTime(default=datetime.utcnow())


class Room(Model):
    id = columns.UUID(primary_key=True, partition_key=True, default=uuid.uuid4)
    room_key = columns.Text(max_length=10) # h.encode(int(time.time()*10))
    title = columns.Text(max_length=50)
    description = columns.Text()
    password = columns.Text()
    created_time = columns.DateTime(default=datetime.utcnow())


class Message(Model):
    id = columns.UUID(primary_key=True, partition_key=True, default=uuid.uuid4)
    timestamp = columns.DateTime(index=True, default=datetime.utcnow())
    content = columns.Text()
    room = columns.UUID()
    user = columns.UUID()
    likes = columns.Counter()
    dismissed = columns.Boolean()

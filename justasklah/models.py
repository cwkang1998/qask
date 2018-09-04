from cassandra.cqlengine.models import Model, columns

class User(Model):
    room = columns.Text()

class Room(Model):
    uid = columns.UUID()

class Chat(Model):
    timestamp = columns.DateTime()
    content = columns.Text()
    user = columns.Text()
    likes = columns.Counter()
    dislikes = columns.Counter()

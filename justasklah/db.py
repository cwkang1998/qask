from datetime import datetime, date
from json import JSONEncoder

from bson import ObjectId
from flask_pymongo import PyMongo
import isodate as iso
mongo = PyMongo()
'''
The database documents design are as follows:

User
-------------
_id(auto generated)
session_hash
room
created_time

Room
--------------
_id(auto generated)
room_key
mode
created_time
title
description
password

Message
--------------
_id(auto generated)
created_time
content
room
user
user_alias
likes
dismissed
'''


def __init_db(app):
    mongo.init_app(app)
    app.json_encoder = MongoJSONEncoder
    return app


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        return JSONEncoder.default(self, o)

from flask_pymongo import PyMongo

mongo = PyMongo()


def __init_db(app):
    mongo.init_app(app)

'''
The database documents design are as follows:

User
-------------
_id(auto generated)
session_hash
created_time

Room
--------------
_id(auto generated)
room_key
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
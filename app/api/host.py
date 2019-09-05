from . import *
from datetime import datetime
from pymongo import DESCENDING
from hashids import Hashids
from bson import ObjectId
from flask_socketio import emit, Namespace, join_room, send

from ..db import mongo, MongoJSONEncoder

"""
Host defined api
"""


@api_bp.route("/room-create/", methods=["POST"])
def room_create():
    if request.method == "POST":
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        password = data.get("password")
        if None not in [title, description, password]:
            room_id = mongo.db.room.insert_one({
                "room_key": Hashids("room").encode(mongo.db.room.count()),
                "created_time": datetime.utcnow(),
                "title": title,
                "description": description,
                "password": password
            })
            room = mongo.db.room.find_one(
                {"_id": ObjectId(room_id.inserted_id)})
            return jsonify(room), 201
        return jsonify({"error": "title, description and password required."})



# admin list to govern
class MessageSocket(Namespace):

    def __init__(self, namespace=None):
        super().__init__(namespace)

    def on_connect(self):
        room_key = request.headers.get("room")
        session_hash = request.headers.get("session_hash")
        send('connected-ns')
        print("Room key: " + room_key)
        print("Session hash: " + session_hash)
        # TODO check the user in the list
        if session_hash != "undefined":
            # find the entry that has session id with the room id
            # if found, this means the user is authenticated
            user = mongo.db.user.find_one(
                {"session_hash": session_hash, "room": room_key}
            )
            if user:
                emit("auth", {"success": "Successfully authenticated."})
                # joining room
                join_room(room_key)
                # return the latest 20 entries
                cursor = mongo.db.message.find({"room": ObjectId(room_key)}).sort(
                    ("time_created", DESCENDING)).limit(20)
                msgs = []
                for doc in cursor:
                    msgs.append(doc)
                cursor.close()

                # emit a collection of messages
                # initialise interface when start connection (displaying previous data)
                emit("initialise_interface", {"messages": msgs})
        # emit("auth", {"error": "Failed to authenticate!"})
        send("HELLO")
        # TODO require redirecting to password page

    def on_disconnect(self):
        pass  # TODO Change session into extra socket headers for better statelessness

    def on_message(self, data):
        room_key = data["room"]
        message_content = data["messageContent"]
        session_hash = data["session_hash"]
        alias = data["alias"]

        user = mongo.db.user.find_one(
            {"session_hash": session_hash, "room": ObjectId(room_key)}
        )
        room = mongo.db.room.find_one_or_404({"room_key": room_key})
        mongo.db.message.insert_one({
            "room": ObjectId(room.get("_id")),
            "created_time": datetime.utcnow(),
            "content": message_content,
            "likes": 0,
            "dismissed": False,
            "user_alias": alias,
            "user": user
        })
        print("Broadcasting room: " + room_key)
        emit("message", message_content, include_self=True, room=room_key)

    def on_like(self, data):
        print(data)

    def on_editing(self, data):
        print(data)
        emit("edit_title", data, include_self=True)

    def on_edit_title(self, data):
        # TODO onchange listener for the value at frontend
        new_title = data["title"]
        room_key = data["room"]
        room = mongo.db.room.find_one_or_404({"room_key": room_key})
        update_result = mongo.db.room.update_one({"_id": room._id}, {
            "$set": {
                "title": new_title,
            }
        })

        emit("edit_title", new_title, include_self=False, room=room_key)

    def on_edit_description(self, data):
        # TODO onchange listener for the value at frontend
        new_description = data["description"]
        room_key = data["room"]
        room = mongo.db.room.find_one_or_404({"room_key": room_key})
        update_result = mongo.db.room.update_one({"_id": room._id}, {
            "$set": {
                "description": new_description,
            }
        })

        emit("edit_description", new_description, include_self=False, room=room_key)

    def on_dismiss(self, data):
        # TODO
        pass

from . import *
import uuid
from ..db import mongo, MongoJSONEncoder
from datetime import datetime
from bson import ObjectId

"""
User defined api
"""


@api_bp.route("/room-join/", methods=["POST"])
def room_join_password(room_id):
    # TODO this endpoint is used for authenticating user to join the room
    # This is an extra step for room that requires password

    # If authenticated
    data = request.get_json()
    room_key = data.get("room_key")
    password = data.get("password")
    session_hash = data.get("session_hash")

    if room_key:
        # TODO display message at frontend to inform either room key or password is wrong
        room = mongo.db.room.find_one_or_404({"room_key": room_key, "password": password})
        res_code = 404
        if room is None:
            return jsonify({"error": "Room key or password is wrong"}), res_code

        # assign a session_hash if not
        # before redirect at frontend, check there exists a session hash, if not assign one
        if session_hash == "undefined":
            session_hash = uuid.uuid4()

        user = mongo.db.user.find_one(
            {"session_hash": session_hash, "room": ObjectId(room.get("_id"))})

        res_code = 200
        if user is None:
            user = mongo.db.user.insert_one({
                "session_hash": session_hash,
                "room": ObjectId(room.get("_id")),
                "admin": False,
                "created_time": datetime.utcnow()
            })
            res_code = 201
        return jsonify(user), res_code

    return jsonify({"error": "room_key is required."}), 404

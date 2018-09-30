from base64 import b64encode
from datetime import datetime
from hashids import Hashids
from flask import Blueprint, jsonify, request
from bson import ObjectId
from flask_socketio import send, emit, disconnect, Namespace

from .db import mongo, MongoJSONEncoder

api_bp = Blueprint('api', __name__, url_prefix='/')


@api_bp.route("/room", methods=["POST"])
def room_create():
    if request.method == "POST":
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        password = data.get("password")

        if(title is not None and
           description is not None and
           password is not None):
            room_id = mongo.db.room.insert_one({
                "room_key": Hashids("room").encode(mongo.db.room.count()),
                "mode": "normal",
                "created_time": datetime.utcnow(),
                "title": title,
                "description": description,
                "password": password
            })
            room = mongo.db.room.find_one(
                {"_id": ObjectId(room_id.inserted_id)})
            return jsonify(room), 201
        return jsonify({"error": "title, description and password required."})


@api_bp.route("/room/<ObjectId:room_id>", methods=["PUT"])
def room_edit(room_id):
    room = mongo.db.room.find_one_or_404({"_id": room_id})
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    password = data.get("password")
    mode = data.get("mode")
    if(title is None):
        title = room._id
    if(description is None):
        description = room.description
    if(password is None):
        password = room.password
    if(mode is None):
        mode = room.mode
    update_result = mongo.db.room.update_one({"_id": room_id}, {
        "mode": mode,
        "title": title,
        "description": description,
        "password": password
    })
    if(update_result.modified_count == 1):
        result = mongo.db.room.find_one({"_id": room_id})
        return jsonify(result), 200
    return jsonify({"error": "Update failed. Please try again"}), 404


@api_bp.route("/room/join", methods=["POST"])
def room_join():
    data = request.get_json()
    room_key = data.get("room_key")
    password = data.get("password")
    if(room_key is not None):
        room = mongo.db.room.find_one_or_404({"room_key": room_key})
        session_hash = (
            b64encode((room_key+request.remote_addr).encode())).decode("utf-8")
        user = mongo.db.user.find_one(
            {"session_hash": session_hash, "room": ObjectId(room.get("_id"))})
        res_code = 200
        is_admin = False
        if(user is None):
            if(password is not None):
                if(room.get("password") == password):
                    is_admin = True
                else:
                    return jsonify({"error": "Invalid admin password."}), 403
            result = mongo.db.user.insert_one({
                "session_hash": session_hash,
                "room": ObjectId(room.get("_id")),
                "admin": is_admin,
                "created_time": datetime.utcnow()
            })
            res_code = 201
            user = mongo.db.user.find_one(
                {"_id": ObjectId(result.inserted_id)})
        return jsonify(user), res_code
    return jsonify({"error": "room_key is required."}), 404


@api_bp.route("/room/<ObjectId:room_id>/users", methods=["GET"])
def room_users(room_id):
    cur = mongo.db.user.find({"_id": room_id})
    users = []
    for doc in cur:
        users.append(doc)
    cur.close()
    return jsonify(users), 200


class MessageSocket(Namespace):

    def on_connect(self):
        room_id = request.headers.get("room")
        session_hash = request.headers.get("session_hash")
        if(room_id is not None and session_hash is not None):
            user = mongo.db.user.find_one(
                {"session_hash": session_hash, "room": ObjectId(room_id)})
            if(user is not None):
                emit("auth", {"success": "Connected."})
                cur = mongo.db.message.find({"room": ObjectId(room_id)})
                msgs = []
                for doc in cur:
                    msgs.append(doc)
                cur.close()
                emit("message", MongoJSONEncoder().encode({"messages": msgs}))
        emit("auth", {"error": "Fail to authenticate."}, callback=disconnect)

    def on_disconnect(self):
        pass  # todo: Change session into extra socket headers for better statelessness

    def on_message(self, data):
        print(data)
        # emit("message", jsonify(data), broadcast=True, include_self=True)

    def on_like(self, data):
        print(data)

    def on_dismiss(self, data):
        print(data)

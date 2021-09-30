from datetime import datetime
from typing import Any, Dict
import uuid

from hashids import Hashids
from pymongo import DESCENDING
from bson import ObjectId
from flask import Blueprint, jsonify, request
import flask_socketio as fsio


from .db import mongo, MongoJSONEncoder


def setupApi(app, socketio):
    api_bp = Blueprint("api", __name__, url_prefix="/")

    @api_bp.route("/room", methods=["POST"])
    def create_room():
        data = request.get_json()
        if not data:
            return {"error": "title, description and password required."}, 400

        title = data.get("title")
        description = data.get("description")
        password = data.get("password")
        if title and description and password:
            room_id = mongo.db.room.insert_one(
                {
                    "room_key": Hashids("room").encode(mongo.db.room.count()),
                    "created_time": datetime.utcnow(),
                    "title": title,
                    "description": description,
                    "password": password,
                }
            )
            room = mongo.db.room.find_one({"_id": ObjectId(room_id.inserted_id)})
            return jsonify(room), 201
        return {"error": "title, description and password required."}, 400

    # General endpoints
    @api_bp.route("/room/<string:room_key>", methods=["GET"])
    def get_room(room_key):
        res_code = 404

        if room_key:
            res_code = 200
            room = mongo.db.room.find_one_or_404({"room_key": room_key})
            room = jsonify(room)
            del room["password"]
            return room, res_code

        return {"error": "room_key is required."}, res_code

    @api_bp.route("/room/<string:room_key>", methods=["POST"])
    def join_room(room_key):
        res_code = 400

        data = request.get_json()
        if not data and not room_key:
            return {"error": "session_key and room_key is required."}, res_code

        session_key = data.get("session_key", None)

        if room_key:
            room = mongo.db.room.find_one_or_404({"room_key": room_key})

            # assign a session_key if not
            # before redirect at frontend, check there exists a session hash, if not assign one
            user = None
            if not session_key:
                session_key = uuid.uuid4()
                user = mongo.db.user.insert_one(
                    {
                        "session_key": session_key,
                        "room": ObjectId(room.get("_id")),
                        "created_time": datetime.utcnow(),
                    }
                )
                res_code = 201
            else:
                user = mongo.db.user.find_one(
                    {"session_key": session_key, "room": ObjectId(room.get("_id"))}
                )
                res_code = 200
            return jsonify(user), res_code

        return {"error": "session_key and room_key is required."}, res_code

    # TODO: Admin endpoints

    # Socketio endpoints
    @socketio.on("message", namespace="/message-channel")
    def socketio_messaging(data: Dict[str, Any]):

        session_key = data.get("session_key", None)
        room_key = data.get("room_key", None)
        message = data.get("message", None)
        created_time = datetime.utcnow()

        if session_key and room_key and message:
            room = mongo.db.room.find_one({"room_key": room_key})
            if room:
                mongo.db.room.update_one(
                    {"_id": room._id}, {"$push": {"messages": message}}, upsert=True
                )
                fsio.emit("message", {room_key, message, created_time}, broadcast=True)
                return
        fsio.emit("error", "Failed to send message")

    app.register_blueprint(api_bp)

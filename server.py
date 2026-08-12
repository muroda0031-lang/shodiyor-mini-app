from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import random
import string
import os

app = Flask(__name__)
CORS(app)

rooms = {}


def make_code():
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=4)
    )


@app.route("/")
def home():
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        "kto_ya.html"
    )


@app.route("/create", methods=["POST"])
def create_room():
    data = request.get_json()
    name = data.get("name", "Игрок")

    code = make_code()

    while code in rooms:
        code = make_code()

    rooms[code] = {
        "players": [name]
    }

    return jsonify({
        "code": code,
        "players": rooms[code]["players"]
    })


@app.route("/join", methods=["POST"])
def join_room():
    data = request.get_json()

    code = data.get("code", "").upper()
    name = data.get("name", "Игрок")

    if code not in rooms:
        return jsonify({"error": "Комната не найдена"}), 404

    if len(rooms[code]["players"]) >= 8:
        return jsonify({"error": "Комната заполнена"}), 400

    rooms[code]["players"].append(name)

    return jsonify({
        "code": code,
        "players": rooms[code]["players"]
    })


@app.route("/room/<code>")
def get_room(code):
    code = code.upper()

    if code not in rooms:
        return jsonify({"error": "Комната не найдена"}), 404

    return jsonify({
        "code": code,
        "players": rooms[code]["players"]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
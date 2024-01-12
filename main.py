import os
import random
from string import ascii_letters
from flask import Flask, request, render_template, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET")
socketio = SocketIO(app)


def code_generator(length: int, codes_list: list[str]) -> str:  # Generate code for chat-room
    while True:
        proto_code = [random.choice(ascii_letters) for _ in range(length)]
        room_code = ''.join(proto_code).upper()
        if room_code not in codes_list:  # Check if generate room code is in existing list of room codes
            return room_code


rooms_db = {}  # Mock DB for persistence


@app.route("/", methods=["GET", "POST"])  # ROUTES
def home():
    session.clear()
    if request.method == "POST":
        name_input_value = request.form.get('name_input')
        code_input_value = request.form.get('code_input')
        join_btn_value = request.form.get('join_btn', False)
        create_btn_value = request.form.get('create_btn', False)
        if not name_input_value:
            return render_template("home.html",
                                   error="You forgot to enter your name!",
                                   code_input_value=code_input_value)
        if create_btn_value != False:
            room_code = code_generator(4, list(rooms_db.keys()))
            new_room = {
                'members': 0,
                'messages': []
            }
            rooms_db[room_code] = new_room
        if join_btn_value != False:
            if not code_input_value:
                return render_template("home.html",
                                       error="You forgot to enter your session code!",
                                       name_input_value=name_input_value)
            if code_input_value not in rooms_db:
                return render_template("home.html",
                                       error="Invalid room code!",
                                       name_input_value=name_input_value)
            room_code = code_input_value
        # CREATE SESSION
        session["room"] = room_code
        session["name"] = name_input_value
        return redirect(url_for("room"))
    else:
        return render_template("home.html")


@app.route("/room")
def room():
    # RETRIEVE SESSION VALUES
    room_session_value = session.get("room")
    name_session_value = session.get("name")
    if name_session_value is None or room_session_value is None or room_session_value not in rooms_db:
        return redirect(url_for("home"))
    message_history = rooms_db[room_session_value]["messages"]
    return render_template("room.html",
                           room_session=room_session_value,
                           name_session=name_session_value,
                           message_history=message_history)


# SOCKETIO EVENTS

@socketio.on("connect")
def connect():
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms_db:
        leave_room(room)
        return

    join_room(room)
    send({"name": name, "message": "joined the room! 🎉"}, to=room)
    rooms_db[room]["members"] += 1
    # print(f"{name} joined room {room}! 🎉")


@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms_db:
        rooms_db[room]["members"] -= 1
        if rooms_db[room]["members"] == 0:
            del rooms_db[room]

    send({"name": name, "message": "left the room... 👋"}, to=room)
    # print(f"{name} left the room {room}... 👋")


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms_db:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms_db[room]["messages"].append(content)
    # print(f"{session.get("name")} said {data['data']}")


if __name__ == "__main__":  # RUN SOCKETIO
    app.run()

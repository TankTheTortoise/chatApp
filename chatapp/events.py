from flask_socketio import emit
from .extensions import socketio

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined")

@socketio.on("new_message")
def handle_new_message(message):
    print(f"Message: {message["message"]}")
    emit("chat", {"username": message["username"] , "message": message["message"]}, broadcast=True)


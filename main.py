from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_folder='frontend')
socket = SocketIO(app)
socket.init_app(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@socket.event
def send_message(data):
    print(data)
    socket.emit("new_message", data)


if __name__ == '__main__':
    socket.run(app, port=6001)


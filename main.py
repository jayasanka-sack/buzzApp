from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import html

app = Flask(__name__, static_folder='frontend')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)


def sanitize_input(input):
    sanitize_str = html.escape(input)
    return sanitize_str


@socketio.on('send_message')
def handle_send_message(data):
    print("Sanitized data is " + sanitize_input(data["message"]))
    data["message"] = sanitize_input(data["message"]) 
    socketio.emit("new_message",data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=6003)


#<button onclick=alert("hello world")>Hello</button>
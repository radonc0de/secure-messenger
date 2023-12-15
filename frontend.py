from flask import Flask, request
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(1)
        count += 1
        socketio.emit('server_message', {'data': f'Server generated message {count}'}, namespace='/test')

@app.route('/')
def index():
    return "WebSocket Server"

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # Start the background thread
    threading.Thread(target=background_thread).start()
    socketio.run(app, debug=True)

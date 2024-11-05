from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def generate_temperature_data():
    while True:
        # Simulating temperature data
        temperature = round(random.uniform(15.0, 30.0), 2)  # Generate a random temperature
        location = "Room A"
        timestamp = time.time()  # Current time in seconds since epoch
        socketio.emit('temperature_data', {'temperature': temperature, 'location': location, 'timestamp': timestamp})
        socketio.sleep(5)  # Emit data every 5 seconds

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(generate_temperature_data)  # Start the temperature data generation in the background

if __name__ == '__main__':
    socketio.run(app, debug=True)

from flask import Flask, jsonify, request, render_template
from ml_model import predict_spoilage
from db import get_sensor_data, insert_sensor_data

app = Flask(__name__)

# Route to render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch sensor data (GET)
@app.route('/api/sensor-data', methods=['GET'])
def fetch_sensor_data():
    data = get_sensor_data()
    return jsonify(data), 200

# Route to receive sensor data (POST)
@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    sensor_data = request.json
    insert_sensor_data(sensor_data)
    return jsonify({"message": "Data received"}), 201

# Route for making predictions based on sensor data (POST)
@app.route('/api/predict', methods=['POST'])
def predict():
    sensor_data = request.json
    result = predict_spoilage(sensor_data)
    return jsonify({"prediction": result}), 200

# Route to handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content response

if __name__ == '__main__':
    app.run(debug=True)

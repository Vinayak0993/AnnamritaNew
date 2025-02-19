from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle

app = Flask(__name__)

# Enable CORS and allow requests from 'http://localhost:3000'
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Load the trained model
with open('spoilage_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.json
        print(f"Received data: {data}")  # Debugging

        # Extract features from the input and convert to appropriate types
        food_type = data['food_type']
        methane_gas_level = float(data['methane_gas_level'])  # Convert to float
        humidity = float(data['humidity'])                      # Convert to float
        temperature = float(data['temperature'])                # Convert to float

        # Prepare the feature vector for the model
        features = [[methane_gas_level, humidity, temperature]]

        # Make prediction
        prediction = model.predict(features)[0]
        print(f"Prediction: {prediction}")  # Debugging

        # Convert prediction to standard type (int)
        prediction = int(prediction)  # Ensure it's a standard Python int

        # Return the result as JSON
        return jsonify({'prediction': prediction})

    except Exception as e:
        print(f"Error: {e}")  # Print the error for debugging
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

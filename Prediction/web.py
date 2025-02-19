from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load model and scaler
model = load_model('food_spoilage_model.h5')
scaler = load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template("process.html")

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    moisture = float(request.form['moisture'])
    gasvalue = float(request.form['gasvalue'])

    # Create a DataFrame for the new data
    new_data = pd.DataFrame({'temperature': [temperature], 'moisture': [moisture], 'gasvalue': [gasvalue]})

    # Preprocess the data
    new_data_processed = preprocess_data(new_data)

    # Make prediction
    prediction = model.predict(new_data_processed)

    # ... (process prediction and return result to template)

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Function to preprocess data
def preprocess_data(data):
    # Convert timestamp to datetime format
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Extract features from timestamp
    data['hour'] = data['timestamp'].dt.hour
    data['day_of_week'] = data['timestamp'].dt.dayofweek

    # Normalize numerical features
    scaler = StandardScaler()
    data[['temperature', 'moisture', 'gasvalue']] = scaler.fit_transform(data[['temperature', 'moisture', 'gasvalue']])

    return data, scaler

# Load data (replace 'data.csv' with your actual file path)
data = pd.read_csv('dattaset.csv')

# Preprocess data
data, scaler = preprocess_data(data)

# Prepare data for LSTM
X = data[['temperature', 'moisture', 'gasvalue', 'hour', 'day_of_week']].values
y = data['spoiled'].values

# Reshape data for LSTM
X = X.reshape(X.shape[0], X.shape[1], 1)

# Create LSTM model
model = Sequential()
model.add(LSTM(units=64, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(LSTM(units=32))
model.add(Dense(units=1, activation='sigmoid'))

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=10, batch_size=32)

# Save model and scaler
model.save('food_spoilage_model.h5')
scaler.save('scaler.pkl')

# Load model and scaler
model = load_model('food_spoilage_model.h5')
scaler = load(open('scaler.pkl', 'rb'))

# Get new data from IoT device
new_data = get_new_data_from_iot_device()

# Preprocess new data
new_data_processed = preprocess_data(new_data)

# Make prediction
prediction = model.predict(new_data_processed)

# Analyze prediction and trigger alerts
if prediction > threshold:
    # Trigger alert or notification
    print("Food item is predicted to be spoiled.")
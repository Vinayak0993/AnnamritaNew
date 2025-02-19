import pickle

with open('ml_model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_spoilage(sensor_data):
    features = [sensor_data['temperature'], sensor_data['humidity'], sensor_data['gasvalue']]
    prediction = model.predict([features])
    return prediction[0]

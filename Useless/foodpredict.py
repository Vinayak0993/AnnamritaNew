import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load data
data = pd.read_csv('sensor_data.csv')

# Preprocess data
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['hour'] = data['timestamp'].dt.hour
data['day_of_week'] = data['timestamp'].dt.dayofweek

scaler = StandardScaler()
data[['temperature', 'moisture', 'gasvalue']] = scaler.fit_transform(data[['temperature', 'moisture', 'gasvalue']])

# Define target variable
data['spoiled'] = 1  # Assuming a binary classification (spoiled vs. not spoiled)

# Split data
X = data[['temperature', 'moisture', 'gasvalue', 'hour', 'day_of_week']]
y = data['spoiled']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

# Evaluate the best model
y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Best Parameters:", best_params)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Make predictions
new_data = pd.DataFrame({'temperature': [32], 'moisture': [1200], 'gasvalue': [2500], 'hour': [18], 'day_of_week': [1]})

prediction = best_model.predict(new_data)
print("Prediction:", prediction)
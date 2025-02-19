import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle

# Load your dataset
data = pd.read_csv("dattaset_csv.csv")

# Drop unnecessary columns
data.drop(columns=['id', 'timestamp'], inplace=True)

# Convert target variable to numeric values using mapping
label_mapping = {"not spoiled": 0, "spoiled": 1}
data['spoiled / not spoiled'] = data["spoiled / not spoiled"].apply(lambda x: label_mapping[x])

# Check for any non-numeric entries and convert relevant columns to numeric, coercing errors to NaN
data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce')
data['moisture'] = pd.to_numeric(data['moisture'], errors='coerce')
data['gasvalue'] = pd.to_numeric(data['gasvalue'], errors='coerce')

# Check for missing values in the relevant columns
print(data[['temperature', 'moisture', 'gasvalue']].isnull().sum())  # Check for NaNs

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Extract features and target variable
X = data[['temperature', 'moisture', 'gasvalue']]
y = data['spoiled / not spoiled']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Save the trained model
with open('spoilage_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# test_virality_model.py

import joblib
import numpy as np

# Load the trained Virality Prediction model
model = joblib.load("backend/models/virality_model.pkl")

# Sample data with varied inputs for testing
sample_data_list = [
    np.array([[2000, 300, 5.2]]),    # Lower engagement
    np.array([[8000, 1200, 9.1]]),   # Higher engagement
    np.array([[4500, 700, 6.0]])     # Moderate engagement
]

# Predict and display virality score for each sample
for i, sample_data in enumerate(sample_data_list, start=1):
    prediction = model.predict(sample_data)
    print(f"Virality Prediction {i} (Virality Score):", prediction[0])
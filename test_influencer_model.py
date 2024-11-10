# test_influencer_model.py

import joblib
import numpy as np

# Load the trained Influencer Identification model
model = joblib.load("backend/models/influencer_model.pkl")

# Sample data with varied inputs for testing
sample_data_list = [
    np.array([[50000, 150, 2000, 150, 50, 8.5]]),  # Typical influencer-like engagement
    np.array([[1000, 20, 50, 10, 2, 2.1]]),       # Low engagement, likely not an influencer
    np.array([[200000, 500, 15000, 1000, 300, 9.9]]) # High engagement, strong influencer profile
]

# Predict and display influencer status for each sample
for i, sample_data in enumerate(sample_data_list, start=1):
    prediction = model.predict(sample_data)
    print(f"Influencer Prediction {i} (1 = Influencer, 0 = Not Influencer):", prediction[0])
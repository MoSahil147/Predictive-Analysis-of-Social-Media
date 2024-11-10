# test_diffusion_model.py

import joblib
import numpy as np

# Load the trained Diffusion Prediction model
model = joblib.load("backend/models/diffusion_model.pkl")

# Sample data with varied inputs for testing
sample_data_list = [
    np.array([[300, 50, 20, 4.0]]),     # Lower spread, likely not misinformation
    np.array([[5000, 2000, 1500, 9.5]]), # High spread, potential misinformation
    np.array([[1000, 300, 200, 6.8]])   # Moderate spread, uncertain misinformation
]

# Predict and display misinformation status for each sample
for i, sample_data in enumerate(sample_data_list, start=1):
    prediction = model.predict(sample_data)
    print(f"Misinformation Prediction {i} (1 = Misinformation, 0 = Not Misinformation):", prediction[0])
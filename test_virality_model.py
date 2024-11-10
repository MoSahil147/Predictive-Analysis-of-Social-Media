import joblib

# Load the trained model
model = joblib.load('backend/models/virality_model.pkl')

# Get user input for each feature needed for virality prediction
print("Enter values for Virality Prediction:")
likes = int(input("Number of Likes (e.g., 100): "))
shares = int(input("Number of Shares (e.g., 15): "))
comments = int(input("Number of Comments (e.g., 20): "))
weak_ties = float(input("Weak Ties Score (e.g., 0.8): "))

# Prepare the input data
sample_data = [[likes, shares, comments, weak_ties]]

# Make a prediction and display the result as a percentage
probability = model.predict_proba(sample_data)[0][1]
print(f"Virality Prediction: {probability * 100:.2f}%")
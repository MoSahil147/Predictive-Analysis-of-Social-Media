import joblib

# Load the trained model
model = joblib.load('backend/models/diffusion_model.pkl')

# Get user input for each feature needed for misinformation prediction
print("Enter values for Diffusion Prediction:")
likes = int(input("Number of Likes (e.g., 300): "))
shares = int(input("Number of Shares (e.g., 25): "))
comments = int(input("Number of Comments (e.g., 40): "))
engagement_rate = float(input("Engagement Rate (e.g., 5.0): "))

# Prepare the input data
sample_data = [[likes, shares, comments, engagement_rate]]

# Make a prediction and display the result as a percentage
probability = model.predict_proba(sample_data)[0][1]
print(f"Misinformation Prediction: {probability * 100:.2f}%")
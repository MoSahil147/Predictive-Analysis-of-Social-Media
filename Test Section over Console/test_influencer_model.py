import joblib

# Load the trained model
model = joblib.load('backend/models/influencer_model.pkl')

# Get user input for each feature needed for influencer identification
print("Enter values for Influencer Identification:")
followers = int(input("Number of Followers (e.g., 1000): "))
posts = int(input("Number of Posts (e.g., 50): "))
likes = int(input("Average Likes per Post (e.g., 100): "))
comments = int(input("Average Comments per Post (e.g., 10): "))
shares = int(input("Average Shares per Post (e.g., 5): "))
engagement_rate = float(input("Engagement Rate (e.g., 3.5): "))

# Prepare the input data
sample_data = [[followers, posts, likes, comments, shares, engagement_rate]]

# Make a prediction and display the result as a percentage
probability = model.predict_proba(sample_data)[0][1]
print(f"Influencer Prediction: {probability * 100:.2f}%")
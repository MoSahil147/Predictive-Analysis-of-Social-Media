import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_virality_model():
    # Load dataset (replace with actual path and data)
    data = pd.DataFrame({
        "likes": [100, 200, 300],
        "shares": [10, 20, 30],
        "comments": [5, 15, 25],
        "weak_ties": [0.5, 0.7, 0.8],
        "virality_score": [40, 50, 60]  # Placeholder target column
    })

    X = data[["likes", "shares", "comments", "weak_ties"]]
    y = data["virality_score"]

    model = LinearRegression()
    model.fit(X, y)

    # Save the model
    MODEL_DIR = os.path.join("backend", "models")
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, os.path.join(MODEL_DIR, "virality_model.pkl"))
    print("Model trained and saved to backend/models/virality_model.pkl")

if __name__ == "__main__":
    train_virality_model()
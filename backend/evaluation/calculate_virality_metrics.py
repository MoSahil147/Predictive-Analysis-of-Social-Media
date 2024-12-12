# Import necessary libraries
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.virality_preprocess import preprocess_data

def evaluate_virality_model():
    """
    Evaluate the Virality Prediction Model on test data.
    """
    # Load the trained model
    model_path = 'backend/models/virality_model.pkl'
    virality_model = joblib.load(model_path)

    # Load and preprocess the test dataset
    test_data = pd.read_csv('backend/data/virality_data.csv')
    X_test, y_test = preprocess_data(test_data)

    # Make predictions
    y_pred = virality_model.predict(X_test)

    # Calculate evaluation metrics
    metrics = {
        "Mean Squared Error (MSE)": mean_squared_error(y_test, y_pred),
        "R2 Score": r2_score(y_test, y_pred)
    }

    # Print results
    print("Virality Model Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")

if __name__ == "__main__":
    evaluate_virality_model()
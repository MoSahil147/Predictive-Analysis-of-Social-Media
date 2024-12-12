from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
import joblib
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.influencer_preprocess import preprocess_data

def evaluate_influencer_model():
    """
    Evaluate the Influencer Identification Model on test data.
    """
    try:
        # Load the trained model
        print("Loading model...")
        model_path = 'backend/models/influencer_model.pkl'
        influencer_model = joblib.load(model_path)
        print("Model loaded successfully.")

        # Load and preprocess the test dataset
        print("Loading test data...")
        test_data = pd.read_csv('backend/data/influencer_data.csv')
        print(f"Test data shape: {test_data.shape}")

        print("Preprocessing data...")
        X_test, y_test = preprocess_data(test_data)
        print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

        # Make predictions
        print("Making predictions...")
        y_pred = influencer_model.predict(X_test)
        y_pred_proba = influencer_model.predict_proba(X_test)[:, 1]
        print("Predictions made successfully.")

        # Calculate evaluation metrics
        print("Calculating metrics...")
        metrics = {
            "Accuracy": accuracy_score(y_test, y_pred),
            "F1 Score": f1_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "AUROC": roc_auc_score(y_test, y_pred_proba),
        }

        print("Influencer Model Metrics:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.2f}")

    except Exception as e:
        print(f"Error during evaluation: {e}")

if __name__ == "__main__":
    evaluate_influencer_model()


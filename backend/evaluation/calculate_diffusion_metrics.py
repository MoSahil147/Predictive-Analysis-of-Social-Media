from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
import joblib
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.diffusion_preprocess import preprocess_data

def evaluate_diffusion_model():
    """
    Evaluate the Diffusion Prediction Model on test data.
    """
    # Load the trained model
    model_path = 'backend/models/diffusion_model.pkl'
    diffusion_model = joblib.load(model_path)

    # Load and preprocess the test dataset
    test_data = pd.read_csv('backend/data/diffusion_data.csv')
    X_test, y_test = preprocess_data(test_data)

    # Make predictions
    y_pred_proba = diffusion_model.predict_proba(X_test)[:, 1]  # Get probability scores for AUROC

    # Adjust the decision threshold for more sensitive predictions (recall)
    threshold = 0.3  # Lower threshold to increase recall
    y_pred_adjusted = (y_pred_proba > threshold).astype(int)

    # Calculate evaluation metrics
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred_adjusted),
        "F1 Score": f1_score(y_test, y_pred_adjusted),
        "Precision": precision_score(y_test, y_pred_adjusted),
        "Recall": recall_score(y_test, y_pred_adjusted),
        "AUROC": roc_auc_score(y_test, y_pred_proba),
    }

    # Print results
    print("Diffusion Model Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")

if __name__ == "__main__":
    evaluate_diffusion_model()




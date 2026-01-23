## Import preprocessing functions and necessary libraries
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.influencer_preprocess import load_data, preprocess_data
from xgboost import XGBClassifier
import joblib  ## For saving the trained model

def train_model():
    ## Load the dataset
    df = load_data('backend/data/influencer_data.csv')

    ## Preprocess data into features and labels
    X, y = preprocess_data(df)

    ## Split data for evaluation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    ## Train the model
    model = XGBClassifier()
    model.fit(X_train, y_train)

    ## Model evaluation
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    class_report = classification_report(y_test, y_pred)

    report = (
        f"Accuracy: {accuracy}\n"
        f"Precision: {precision}\n"
        f"Recall: {recall}\n"
        f"F1 Score: {f1}\n\n"
        f"Classification Report:\n{class_report}"
    )

    print("--- Influencer Model Evaluation ---")
    print(report)

    ## Save evaluation report
    with open('backend/evaluation/reports/influencer_report.txt', 'w') as f:
        f.write(report)

    ## Retrain on full dataset
    full_model = XGBClassifier()
    full_model.fit(X, y)

    ## Save final model
    joblib.dump(full_model, 'backend/scalers/influencer_model.pkl')
    print("Influencer model trained and saved.")

if __name__ == "__main__":
    train_model()
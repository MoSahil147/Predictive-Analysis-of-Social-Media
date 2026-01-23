## Import required libraries
import sys
import os
import lightgbm as lgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.diffusion_preprocess import load_data, preprocess_data

def train_model():
    ## Load dataset
    df = load_data('backend/data/diffusion_data.csv')

    ## Preprocess dataset
    X, y = preprocess_data(df)

    ## Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    ## Handle class imbalance
    pos_count = (y_train == 1).sum()
    neg_count = (y_train == 0).sum()
    scale_pos_weight = neg_count / pos_count if pos_count > 0 else 1

    ## Train LightGBM model
    model = lgb.LGBMClassifier(scale_pos_weight=scale_pos_weight)
    model.fit(X_train, y_train)

    ## Predictions
    y_pred = model.predict(X_test)

    ## Metrics
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

    print("--- Diffusion Model Evaluation ---")
    print(report)

    ## Save report
    with open('backend/evaluation/reports/diffusion_report.txt', 'w') as f:
        f.write(report)

    ## Retrain on full dataset
    full_model = lgb.LGBMClassifier(scale_pos_weight=scale_pos_weight)
    full_model.fit(X, y)

    ## Save model
    joblib.dump(full_model, 'backend/scalers/diffusion_model.pkl')
    print("Diffusion model trained and saved.")

if __name__ == "__main__":
    train_model()
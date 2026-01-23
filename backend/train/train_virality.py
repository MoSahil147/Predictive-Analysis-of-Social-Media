## Import preprocessing functions and libraries
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.virality_preprocess import load_data, preprocess_data
from xgboost import XGBRegressor
import joblib

def train_virality_model():
    ## Load dataset
    df = load_data('backend/data/virality_data.csv')

    ## Preprocess data
    X, y = preprocess_data(df)

    ## Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    ## Initialize model
    model = XGBRegressor(
        objective='reg:squarederror',
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6
    )

    ## Train model
    model.fit(X_train, y_train)

    ## Predictions
    y_pred = model.predict(X_test)

    ## Metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    report = (
        f"Mean Squared Error: {mse}\n"
        f"R2 Score: {r2}"
    )

    print("--- Virality Model Evaluation ---")
    print(report)

    ## Save report
    with open('backend/evaluation/reports/virality_report.txt', 'w') as f:
        f.write(report)

    ## Retrain on full dataset
    full_model = XGBRegressor(
        objective='reg:squarederror',
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6
    )
    full_model.fit(X, y)

    ## Save model
    joblib.dump(full_model, 'backend/models/virality_model.pkl')
    print("Virality prediction model trained and saved.")

if __name__ == "__main__":
    train_virality_model()
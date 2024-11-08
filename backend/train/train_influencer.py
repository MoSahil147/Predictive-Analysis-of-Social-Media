# Corrected path for importing preprocess
from backend.preprocess.influencer_preprocess import load_data, preprocess_data
from xgboost import XGBClassifier
import joblib

def train_model():
    # Corrected path for loading data file
    df = load_data('backend/data/influencer_data.csv')

    X, y = preprocess_data(df)
    model = XGBClassifier()
    model.fit(X, y)
    joblib.dump(model, 'backend/models/influencer_model.pkl')
    print("Influencer model trained and saved.")

if __name__ == "__main__":
    train_model()

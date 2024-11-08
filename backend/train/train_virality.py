# Corrected path for importing preprocess
from backend.preprocess.virality_preprocess import load_data, preprocess_data
from lightgbm import LGBMClassifier
import joblib

def train_model():
    # Corrected path for loading data file
    df = load_data('backend/data/virality_data.csv')

    X, y = preprocess_data(df)
    model = LGBMClassifier()
    model.fit(X, y)
    joblib.dump(model, 'backend/models/virality_model.pkl')
    print("Virality model trained and saved.")

if __name__ == "__main__":
    train_model()

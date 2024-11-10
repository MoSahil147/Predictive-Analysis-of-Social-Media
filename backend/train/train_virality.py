import joblib
from lightgbm import LGBMClassifier
from backend.preprocess.virality_preprocess import load_data, preprocess_data

def train_model():
    # Load and preprocess the data
    df = load_data('backend/data/virality_data.csv')
    X, y = preprocess_data(df)  # Now includes 'weak_ties'

    # Define and train the model
    model = LGBMClassifier()
    model.fit(X, y)

    # Save the model
    joblib.dump(model, 'backend/models/virality_model.pkl')
    print("Virality model trained and saved.")

if __name__ == "__main__":
    train_model()
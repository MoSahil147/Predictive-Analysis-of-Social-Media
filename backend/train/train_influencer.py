# Import preprocessing functions and necessary libraries
from backend.preprocess.influencer_preprocess import load_data, preprocess_data  # For data loading and preprocessing
from xgboost import XGBClassifier  # Import XGBoost for training the model
import joblib  # For saving the trained model

def train_model():
    # Load the dataset from the specified CSV file
    df = load_data('backend/data/influencer_data.csv')

    # Preprocess the data into features (X) and target (y)
    X, y = preprocess_data(df)

    # Initialize and train the XGBoost classifier
    model = XGBClassifier()
    model.fit(X, y)

    # Save the trained model to the specified path
    joblib.dump(model, 'backend/models/influencer_model.pkl')
    print("Influencer model trained and saved.")

# Execute the training function when the script is run directly
if __name__ == "__main__":
    train_model()

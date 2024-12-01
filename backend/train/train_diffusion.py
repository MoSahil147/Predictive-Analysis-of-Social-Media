# Import preprocessing functions and necessary libraries
from backend.preprocess.diffusion_preprocess import load_data, preprocess_data  # For data loading and preprocessing
import lightgbm as lgb  # Import LightGBM for training the model
import joblib  # For saving the trained model

def train_model():
    # Load the dataset from the specified CSV file
    df = load_data('backend/data/diffusion_data.csv')

    # Preprocess the data into features (X) and target (y)
    X, y = preprocess_data(df)
    
    # Initialize and train a LightGBM classifier for diffusion modeling
    model = lgb.LGBMClassifier()
    model.fit(X, y)
    
    # Save the trained model to the specified path
    joblib.dump(model, 'backend/models/diffusion_model.pkl')
    print("Diffusion model trained and saved.")

# Execute the training function when the script is run directly
if __name__ == "__main__":
    train_model()

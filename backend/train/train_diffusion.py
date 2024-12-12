import sys
import os
import lightgbm as lgb  # Import LightGBM for training the model
import joblib  # For saving the trained model
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.diffusion_preprocess import load_data, preprocess_data

def train_model():
    # Load the dataset from the specified CSV file
    df = load_data('backend/data/diffusion_data.csv')

    # Preprocess the data into features (X) and target (y)
    X, y = preprocess_data(df)

    # Calculate the class weights
    # We calculate the `scale_pos_weight` based on the ratio of negative to positive class
    pos_class_weight = (y == 1).sum()
    neg_class_weight = (y == 0).sum()
    scale_pos_weight = neg_class_weight / pos_class_weight

    # Initialize and train a LightGBM classifier for diffusion modeling
    model = lgb.LGBMClassifier(scale_pos_weight=scale_pos_weight)
    model.fit(X, y)

    # Save the trained model to the specified path
    joblib.dump(model, 'backend/models/diffusion_model.pkl')
    print("Diffusion model trained and saved.")

# Execute the training function when the script is run directly
if __name__ == "__main__":
    train_model()




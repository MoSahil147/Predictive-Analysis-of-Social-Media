# Import preprocessing functions and necessary libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.preprocess.virality_preprocess import load_data, preprocess_data

from xgboost import XGBRegressor  # Import XGBoost for training the regression model
import joblib  # Library for saving the trained model

def train_virality_model():
    """
    Train the virality prediction model.
    """
    # Step 1: Load the dataset from the specified CSV file
    df = load_data('backend/data/virality_data.csv')  # Ensure the path points to the correct CSV file
    
    # Step 2: Preprocess the data
    # Split the dataset into features (X) and target (y) using preprocessing functions
    X, y = preprocess_data(df)

    # Step 3: Initialize and configure the XGBoost regressor
    model = XGBRegressor(
        objective='reg:squarederror',  # Objective function for regression problems
        n_estimators=100,  # Number of trees in the ensemble
        learning_rate=0.1,  # Step size for weight updates
        max_depth=6  # Maximum depth of each tree
    )
    
    # Step 4: Train the model on the preprocessed data
    model.fit(X, y)  # Fit the model using features (X) and target (y)

    # Step 5: Save the trained model to the specified path
    joblib.dump(model, 'backend/models/virality_model.pkl')  # Save the model as a .pkl file for reuse
    print("Virality prediction model trained and saved.")  # Inform the user that the model is saved

# Entry point for the script
if __name__ == "__main__":
    # Execute the training function only if the script is run directly
    train_virality_model()
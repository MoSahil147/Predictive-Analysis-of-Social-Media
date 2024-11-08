# backend/train/train_diffusion.py

from backend.preprocess.diffusion_preprocess import load_data, preprocess_data

import lightgbm as lgb
import joblib

def train_model():
    df = load_data('backend/data/diffusion_data.csv')
    X, y = preprocess_data(df)
    
    # LightGBM model for diffusion (misinformation detection)
    model = lgb.LGBMClassifier()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, 'backend/models/diffusion_model.pkl')
    print("Diffusion model trained and saved.")

if __name__ == "__main__":
    train_model()

# backend/preprocess/diffusion_preprocess.py

import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    # Select features
    X = df[['likes', 'shares', 'comments', 'engagement_rate']]
    # Update the target to match 'is_misinformation'
    y = df['is_misinformation']
    return X, y

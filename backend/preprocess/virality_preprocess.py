import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    X = df[['likes', 'shares', 'comments', 'weak_ties']]  # Features for virality prediction
    y = df['virality_label']  # Target column
    return X, y
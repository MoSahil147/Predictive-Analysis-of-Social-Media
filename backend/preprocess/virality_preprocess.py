import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    X = df[['likes', 'shares', 'comments']]
    y = df['is_viral']
    return X, y

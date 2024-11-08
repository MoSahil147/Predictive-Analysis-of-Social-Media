import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    X = df[['followers', 'posts', 'likes', 'comments', 'shares', 'engagement_rate']]
    y = df['is_influencer']
    return X, y

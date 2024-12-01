import pandas as pd  # For data manipulation and analysis

# Load data from a CSV file
def load_data(filepath):
    return pd.read_csv(filepath)

# Preprocess the data for model input
def preprocess_data(df):
    X = df[['likes', 'shares', 'comments', 'weak_ties']]  # Features
    y = df['virality_label']  # Target variable
    return X, y

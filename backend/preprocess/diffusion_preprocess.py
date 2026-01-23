import pandas as pd

## This function loads data from a CSV file into a pandas DataFrame.
def load_data(filepath):
    ## It takes the file path as input and returns the loaded DataFrame.
    return pd.read_csv(filepath)

## This function preprocesses the data for the diffusion model.
def preprocess_data(df):
    ## It selects the features (X) and the target variable (y) from the DataFrame.
    # Select features
    X = df[['likes', 'shares', 'comments', 'engagement_rate']]
    ## The target variable is 'is_misinformation', which indicates whether a post is misinformation or not.
    y = df['is_misinformation']
    return X, y

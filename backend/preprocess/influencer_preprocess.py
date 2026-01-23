import pandas as pd

## This function loads data from a CSV file into a pandas DataFrame.
def load_data(filepath):
    ## It takes the file path as input and returns the loaded DataFrame.
    return pd.read_csv(filepath)

## This function preprocesses the data for the influencer model.
def preprocess_data(df):
    ## It selects the features (X) and the target variable (y) from the DataFrame.
    X = df[['followers', 'posts', 'likes', 'comments', 'shares', 'engagement_rate']]
    ## The target variable is 'is_influencer', which indicates whether a user is an influencer or not.
    y = df['is_influencer']
    return X, y

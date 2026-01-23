import pandas as pd

## This function loads data from a CSV file into a pandas DataFrame.
def load_data(filepath):
    ## It takes the file path as input and returns the loaded DataFrame.
    return pd.read_csv(filepath)

## This function preprocesses the data for the virality model.
def preprocess_data(df):
    ## It selects the features (X) and the target variable (y) from the DataFrame.
    X = df[['likes', 'shares', 'comments', 'weak_ties']]
    ## The target variable is 'virality_label', which is a numerical score representing virality.
    y = df['virality_label']
    return X, y

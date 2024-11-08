# utils/batch_processing.py

import numpy as np
import pandas as pd
from typing import Callable, Union

def batch_generator(data: Union[np.ndarray, pd.DataFrame], batch_size: int):
    """
    Generator that yields data in batches.
    
    Parameters:
    - data: The dataset to be split into batches (numpy array or pandas DataFrame).
    - batch_size: Size of each batch.
    
    Yields:
    - Batches of data of specified batch_size.
    """
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def batch_predict(model, data: np.ndarray, batch_size: int, preprocess_func: Callable = None):
    """
    Perform predictions on data in batches to save memory.
    
    Parameters:
    - model: The trained model used for prediction.
    - data: Input data to be predicted on (as numpy array).
    - batch_size: Size of each batch for processing.
    - preprocess_func: Optional preprocessing function to apply to each batch.
    
    Returns:
    - numpy array of predictions for the entire dataset.
    """
    predictions = []
    for batch in batch_generator(data, batch_size):
        if preprocess_func:
            batch = preprocess_func(batch)
        batch_predictions = model.predict(batch)
        predictions.extend(batch_predictions)
    return np.array(predictions)

def batch_process(data: pd.DataFrame, process_func: Callable, batch_size: int):
    """
    Apply a specified processing function to data in batches.
    
    Parameters:
    - data: Input data (pandas DataFrame).
    - process_func: Function to apply to each batch.
    - batch_size: Size of each batch for processing.
    
    Returns:
    - Concatenated results of applying process_func to each batch.
    """
    results = []
    for batch in batch_generator(data, batch_size):
        batch_result = process_func(batch)
        results.append(batch_result)
    return pd.concat(results, ignore_index=True)

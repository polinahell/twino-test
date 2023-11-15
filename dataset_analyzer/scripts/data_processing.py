import pandas as pd

def load_data(file_path):
    """Load the dataset."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Perform data cleaning."""
    # Handle missing values and outliers
    # Convert data types if necessary
    return df
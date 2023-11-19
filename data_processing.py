import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    # Load the dataset
    return pd.read_csv(file_path)

def clean_data(df):
    # Check if the column exists before trying to drop it
    if 'Unnamed: 0' in df.columns:
        df.drop(['Unnamed: 0'], axis=1, inplace=True)

    # Add year and month columns
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df.drop(['date'], axis=1, inplace=True)

    # Convert 'zipcode' to a categorical column
    le = LabelEncoder()
    le.fit(df['zipcode'])
    df['zipcode'] = le.transform(df['zipcode'])

    # Add a 'renovated' column
    df['renovated'] = df['yr_renovated'].apply(lambda x: 0 if x == 0 else 1)
    df.drop(['yr_renovated'], axis=1, inplace=True)

    return df

def get_summary_statistics(df):
    return df.describe()

def get_floor_value_counts(df):
    floor_counts = df['floors'].value_counts()
    floor_counts_dict = floor_counts.to_dict()
    return floor_counts_dict

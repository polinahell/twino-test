import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):

    return pd.read_csv(file_path)

def clean_data(df):
    # Check if the column exists
    if 'Unnamed: 0' in df.columns:
        df.drop(['Unnamed: 0'], axis=1, inplace=True)

    # Add year and month columns
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df.drop(['date'], axis=1, inplace=True)

    # Add a 'renovated' column
    df['renovated'] = df['yr_renovated'].apply(lambda x: 0 if x == 0 else 1)
    df.drop(['yr_renovated'], axis=1, inplace=True)

    return df

def get_summary_statistics(df):
    return df.describe()

def get_deal_volume_over_time_by_criteria(df, criteria):

    # Ensure the specified criteria column exists in the DataFrame
    if criteria not in df.columns:
        return f"Error: '{criteria}' is not a valid criteria column."

    # Group by year, month, and bedrooms, and count the number of deals
    deal_volume = df.groupby(['year', 'month', criteria]).size().reset_index(name='count')

    # Plot the deal volume
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year', y='count', hue=criteria, data=deal_volume)
    plt.title(f'Deal Volume Over Time by {criteria}')
    plt.xlabel('Year')
    plt.ylabel('Number of Deals')
    plt.legend(title=criteria, loc='upper right')
    plt.show()

    return deal_volume


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn import metrics
import os
import tensorflow as tf

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'

def analyze_deal_volume_over_time(df):
    deal_volume = df.groupby(['year', 'month']).agg({'price': ['count', 'sum']}).reset_index()

    # Plot the number of deals over time
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(deal_volume['year'], deal_volume['price']['count'], marker='o')
    plt.title('Number of Deals Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Deals')

    # Plot the total deal amount over time
    plt.subplot(1, 2, 2)
    plt.plot(deal_volume['year'], deal_volume['price']['sum'], marker='o', color='orange')
    plt.title('Total Deal Amount Over Time')
    plt.xlabel('Year')
    plt.ylabel('Total Deal Amount')
    
    plt.tight_layout()
    plt.show()

def analyze_avg_price_per_unit_over_time(df):
    # Calculate average price per unit for deal, sqft, and number of bedrooms
    df['price_per_sqft'] = df['price'] / df['sqft_living']
    df['price_per_bedroom'] = df['price'] / df['bedrooms']

    # Group by year and month
    avg_price_per_unit = df.groupby(['year', 'month']).agg({
        'price': 'mean',
        'price_per_sqft': 'mean',
        'price_per_bedroom': 'mean'
    }).reset_index()

    # Combine 'year' and 'month' into a new column 'month_year'
    avg_price_per_unit['month_year'] = avg_price_per_unit[['year', 'month']].astype(str).agg('-'.join, axis=1)

    # Print the results
    print("Average Price per Unit Over Time:")
    print(avg_price_per_unit)

    # Plot the average values over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='month_year', y='price', label='Average Price per Deal', data=avg_price_per_unit)
    sns.lineplot(x='month_year', y='price_per_sqft', label='Average Price per Sqft', data=avg_price_per_unit)
    sns.lineplot(x='month_year', y='price_per_bedroom', label='Average Price per Bedroom', data=avg_price_per_unit)
    
    plt.title('Average Price per Unit Over Time')
    plt.xlabel('Month-Year')
    plt.ylabel('Average Price')
    plt.legend(title='Unit Type', loc='upper right')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

    return avg_price_per_unit


def analyze_price_distribution(df):
  
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title('Distribution of House Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

def analyze_deal_volume_over_time_by_criteria(df, criteria_column):
    deal_volume_criteria = df.groupby(['year', 'month', criteria_column]).agg({'price': 'count'}).reset_index()

    # Plot the deal volume 
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year', y='price', hue=criteria_column, data=deal_volume_criteria)
    plt.title(f'Deal Volume Over Time by {criteria_column}')
    plt.xlabel('Year')
    plt.ylabel('Number of Deals')
    plt.legend(title=criteria_column, loc='upper right')
    plt.show()


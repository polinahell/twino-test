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

    # Plot the average values over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year', y='value', hue='variable', data=pd.melt(avg_price_per_unit, ['year', 'month']))
    plt.title('Average Price per Unit Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.legend(title='Unit Type', loc='upper right')
    plt.show()



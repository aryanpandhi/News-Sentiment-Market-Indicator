import pandas as pd 
import numpy as np

market_df = pd.read_csv('SPY_market_data.csv')
dates = market_df['Date']
difference = ((market_df['Close'] - market_df['Open'])/market_df['Open'])*100
market_movement = pd.DataFrame({'Date': dates, 'Difference': difference })
print(market_movement.head())
print(market_movement.describe())
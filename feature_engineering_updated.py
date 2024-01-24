
import pandas as pd
import numpy as np

def add_seasonal_features(df):
    # Deriving the 'season' feature based on the month
    seasons = {
        1: 'winter', 2: 'winter', 3: 'spring',
        4: 'spring', 5: 'spring', 6: 'summer',
        7: 'summer', 8: 'summer', 9: 'fall',
        10: 'fall', 11: 'fall', 12: 'winter'
    }
    df['season'] = df['month'].map(seasons)
    return df

def add_temperature_range(df):
    df['temp_range'] = df['high'] - df['low']
    return df

def add_lag_features(df, lag_columns, lag_periods):
    for col in lag_columns:
        for lag in lag_periods:
            df[f'{col}_lag_{lag}'] = df.groupby('city')[col].shift(lag)
    return df

def add_statistical_features(df):
    # Calculating mean, median, and standard deviation for each city and month
    for col in ['high', 'low', 'rainfall', 'snowDays']:
        df[f'{col}_monthly_mean'] = df.groupby(['city', 'month'])[col].transform('mean')
        df[f'{col}_monthly_median'] = df.groupby(['city', 'month'])[col].transform('median')
        df[f'{col}_monthly_std'] = df.groupby(['city', 'month'])[col].transform('std')
    return df

def feature_engineering(df):
    df = add_seasonal_features(df)
    df = add_temperature_range(df)
    df = add_lag_features(df, ['high', 'low', 'rainfall', 'snowDays'], [1, 2, 3])
    df = add_statistical_features(df)
    return df

if __name__ == "__main__":
    # Example usage
    # Here you would load your preprocessed DataFrame
    # Example data (should be replaced with actual preprocessed data)
    df = pd.DataFrame({
        'city': ['CityA', 'CityA', 'CityB', 'CityB'],
        'month': [1, 2, 1, 2],
        'high': [10, 12, 15, 17],
        'low': [1, 3, 5, 7],
        'rainfall': [20, 30, 40, 50],
        'snowDays': [2, 3, 1, 0]
    })
    engineered_df = feature_engineering(df)
    print(engineered_df.head())

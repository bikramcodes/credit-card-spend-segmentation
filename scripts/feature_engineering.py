import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_features(df):
    df['Total_Spend'] = df['PURCHASES'] + df['CASH_ADVANCE']
    df['Payment_to_MinPay'] = df['PAYMENTS'] / (df['MINIMUM_PAYMENTS'] + 1e-5)
    df['Balance_Limit_Ratio'] = df['BALANCE'] / (df['CREDIT_LIMIT'] + 1e-5)
    return df

def scale_features(df):
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled
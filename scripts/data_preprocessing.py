import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def handle_missing_values(df):
    df['MINIMUM_PAYMENTS'] = df['MINIMUM_PAYMENTS'].fillna(df['MINIMUM_PAYMENTS'].median())
    df['CREDIT_LIMIT'] = df['CREDIT_LIMIT'].fillna(df['CREDIT_LIMIT'].median())
    return df

def drop_unnecessary_columns(df):
    df = df.drop('CUST_ID', axis=1)
    return df
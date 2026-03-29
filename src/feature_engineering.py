import pandas as pd

def engineer_features(df):
    df = df.copy()

    # Extract bathrooms safely
    df['bathrooms'] = df['bathrooms_text'].str.extract(r'(\d+\.?\d*)')[0]
    df['bathrooms'] = pd.to_numeric(df['bathrooms'], errors='coerce')

    df = df.drop(columns=['bathrooms_text'])

    # One-hot encode
    df = pd.get_dummies(df, columns=['room_type'], drop_first=True)

    # Fill missing
    df = df.fillna(0)

    return df

import pandas as pd

def engineer_features(df):
    # Convert categorical variables
    df = pd.get_dummies(df, columns=['room_type'], drop_first=True)

    # Extract numeric bathrooms
    df['bathrooms'] = df['bathrooms_text'].str.extract(r'(\d+\.?\d*)').astype(float)
    df = df.drop(columns=['bathrooms_text'])

    return df

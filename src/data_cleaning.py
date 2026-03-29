import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Drop unnecessary columns
    df = df[['price', 'room_type', 'accommodates', 'bathrooms_text',
             'bedrooms', 'beds', 'number_of_reviews', 'review_scores_rating']]

    # Clean price (remove $ and commas)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Handle missing values
    df = df.dropna()

    return df

def save_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = load_data("data/raw/listings.csv")
    df = clean_data(df)
    save_data(df, "data/processed/cleaned.csv")

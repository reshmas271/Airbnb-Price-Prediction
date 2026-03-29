import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

from feature_engineering import engineer_features

def train():
    df = pd.read_csv("data/processed/cleaned.csv")
    df = engineer_features(df)

    X = df.drop("price", axis=1)
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    print(f"MAE: {mae:.2f}")

    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()

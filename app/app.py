import streamlit as st
import pandas as pd
import joblib

# Load model + columns
model, columns = joblib.load("models/model.pkl")

st.title("🏠 Airbnb Price Predictor")

accommodates = st.slider("Accommodates", 1, 10, 2)
bedrooms = st.slider("Bedrooms", 0, 5, 1)
beds = st.slider("Beds", 1, 10, 1)
bathrooms = st.slider("Bathrooms", 1, 5, 1)
reviews = st.slider("Number of Reviews", 0, 500, 10)

room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room"])

# Build input dictionary
data = {
    "accommodates": accommodates,
    "bedrooms": bedrooms,
    "beds": beds,
    "bathrooms": bathrooms,
    "number_of_reviews": reviews,
    "review_scores_rating": 90
}

# Handle one-hot encoding manually
data["room_type_Private room"] = 1 if room_type == "Private room" else 0

# Convert to DataFrame
input_df = pd.DataFrame([data])

# Align columns with training
input_df = input_df.reindex(columns=columns, fill_value=0)

# Predict
prediction = model.predict(input_df)[0]

st.subheader(f"💰 Predicted Price: ${prediction:.2f}")

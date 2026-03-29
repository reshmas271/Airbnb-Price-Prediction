import streamlit as st
import pandas as pd
import joblib

model = joblib.load("../models/model.pkl")

st.title("Airbnb Price Predictor")

accommodates = st.slider("Accommodates", 1, 10, 2)
bedrooms = st.slider("Bedrooms", 0, 5, 1)
beds = st.slider("Beds", 1, 10, 1)
reviews = st.slider("Number of Reviews", 0, 500, 10)

room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room"])

data = pd.DataFrame({
    "accommodates": [accommodates],
    "bedrooms": [bedrooms],
    "beds": [beds],
    "number_of_reviews": [reviews],
    "review_scores_rating": [90],
    "room_type_Private room": [1 if room_type == "Private room" else 0]
})

prediction = model.predict(data)[0]

st.write(f"### Predicted Price: ${prediction:.2f}")

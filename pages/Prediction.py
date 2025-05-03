

import streamlit as st
import pandas as pd
import joblib
import os

def run_prediction():
    st.title("Prediction")

    model_file = st.selectbox("Select a model", [f for f in os.listdir("models") if f.endswith(".pkl")])
    model = joblib.load(os.path.join("models", model_file))

    st.subheader("Input Values for Prediction")
    input_data = {}

    feature_count = st.number_input("Enter number of features", min_value=1, step=1)

    for i in range(int(feature_count)):
        feature_name = st.text_input(f"Feature {i+1} name")
        feature_value = st.number_input(f"Value for {feature_name}")
        input_data[feature_name] = feature_value

    if st.button("Predict"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        st.success(f"Predicted value: {prediction[0]}")

# Run in Streamlit
if __name__ == "__main__":
    run_prediction()

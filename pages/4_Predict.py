import streamlit as st
import pandas as pd
import numpy as np
from data_utils import load_dataset, load_trained_model, preprocess_features
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("🔮 Temperature Prediction")

    model_name = st.selectbox("Choose a trained model", ["random_forest", "gradient_boosting", "ridge", "linear_regression"])
    try:
        model = load_trained_model(model_name)
    except FileNotFoundError:
        st.error("Trained model not found. Please train one first.")
        return

    data = load_dataset()
    feature_cols = [col for col in data.columns if col not in ["avg_max_temp", "year"]]

    user_inputs = {}
    cols = st.columns(3)
    for i, col in enumerate(feature_cols):
        with cols[i % 3]:
            user_inputs[col] = st.number_input(col, float(data[col].min()), float(data[col].max()), float(data[col].median()))

    inputs_df = pd.DataFrame([user_inputs])

    # Preprocess input
    _, _, _, _, scaler = preprocess_features(data)
    inputs_df_scaled = scaler.transform(inputs_df)

    if st.button("Predict Temperature"):
        prediction = model.predict(inputs_df_scaled)
        st.success(f"Predicted Max Temperature: {prediction[0]:.2f}°C")

        # Historical comparison
        st.subheader("📉 Historical Trends")
        fig, ax = plt.subplots()
        sns.lineplot(data=data, x="year", y="avg_max_temp", ax=ax)
        ax.axhline(y=prediction[0], color="red", linestyle="--", label="Prediction")
        ax.set_title("Historical vs Predicted Temperature")
        ax.legend()
        st.pyplot(fig)

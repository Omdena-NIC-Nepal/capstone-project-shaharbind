
import streamlit as st
import joblib
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from data_utils import load_combined_data

def run_model_evaluation():
    st.title("Model Evaluation")

    df = load_combined_data()
    if df is None:
        st.error("Processed data not found. Please run data preprocessing first.")
        return

    target = st.selectbox("Select target variable", df.columns)
    features = st.multiselect("Select feature columns", [col for col in df.columns if col != target])

    if st.button("Evaluate Models"):
        X = df[features]
        y = df[target]

        model_scores = {}
        for model_file in os.listdir("models"):
            if model_file.endswith(".pkl"):
                model_name = model_file.replace(".pkl", "")
                model = joblib.load(os.path.join("models", model_file))
                predictions = model.predict(X)
                mse = mean_squared_error(y, predictions)
                r2 = r2_score(y, predictions)
                model_scores[model_name] = {"MSE": mse, "R²": r2}

        st.subheader("Evaluation Metrics")
        st.write(pd.DataFrame(model_scores).T)

# Run in Streamlit
if __name__ == "__main__":
    run_model_evaluation()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_utils import load_dataset, load_trained_model, preprocess_features

def show():
    st.title("📊 Evaluate Trained Model")

    model_name = st.selectbox("Select a model", ["random_forest", "gradient_boosting", "ridge", "linear_regression"])
    try:
        model = load_trained_model(model_name)
        data = load_dataset()
        _, X_test, _, y_test, _ = preprocess_features(data)
        y_pred = model.predict(X_test)

        st.subheader("1. Actual vs Predicted")
        fig1, ax1 = plt.subplots()
        sns.scatterplot(x=y_test, y=y_pred, ax=ax1)
        ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        st.pyplot(fig1)

        st.subheader("2. Residual Plot")
        residuals = y_test - y_pred
        fig2, ax2 = plt.subplots()
        sns.histplot(residuals, kde=True, ax=ax2)
        st.pyplot(fig2)

        if hasattr(model, "feature_importances_"):
            st.subheader("3. Feature Importances")
            importance = pd.Series(model.feature_importances_, index=data.drop(columns=["avg_max_temp", "year"]).columns)
            fig3, ax3 = plt.subplots()
            importance.sort_values().plot(kind='barh', ax=ax3)
            st.pyplot(fig3)
    except FileNotFoundError:
        st.warning("Model file not found. Train it first.")

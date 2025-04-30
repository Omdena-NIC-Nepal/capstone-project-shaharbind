import streamlit as st
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
from data_utils import load_dataset, preprocess_features, save_trained_model

def show():
    st.title("🧠 Train Machine Learning Model")

    model_options = {
        "Random Forest": RandomForestRegressor,
        "Gradient Boosting": GradientBoostingRegressor,
        "Ridge Regression": Ridge,
        "Linear Regression": LinearRegression
    }

    selected = st.selectbox("Select Algorithm", list(model_options.keys()))
    data = load_dataset()
    X_train, X_test, y_train, y_test, scaler = preprocess_features(data)

    model_params = {}
    if selected == "Random Forest":
        model_params["n_estimators"] = st.slider("Trees", 50, 200, 100)
    elif selected == "Gradient Boosting":
        model_params["n_estimators"] = st.slider("Trees", 50, 200, 100)
        model_params["learning_rate"] = st.slider("Learning Rate", 0.01, 0.5, 0.1)
    elif selected == "Ridge Regression":
        model_params["alpha"] = st.slider("Alpha", 0.1, 10.0, 1.0)

    if st.button("Train Model"):
        Model = model_options[selected]
        model = Model(**model_params)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.success("Model Trained Successfully ✅")

        st.metric("MAE", f"{mean_absolute_error(y_test, y_pred):.2f}")
        st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
        st.metric("R²", f"{r2_score(y_test, y_pred):.2f}")

        save_trained_model(model, selected.lower().replace(" ", "_"))
        st.success("Model Saved 📦")

import streamlit as st
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Temporary replacement for data_utils import (since we're bypassing it)
def load_combined_data():
    sample_data = {
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [6, 7, 8, 9, 10],
        'Feature3': [11, 12, 13, 14, 15],
        'Target': [5, 6, 7, 8, 9]  # Target variable
    }
    return pd.DataFrame(sample_data)

def save_model(model, model_name):
    """
    Save the trained model to the models directory
    """
    model_dir = './models/'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    model_path = os.path.join(model_dir, f'{model_name}.pkl')
    joblib.dump(model, model_path)
    st.success(f"Model saved as {model_path}")
    
def train_model(model_name, X_train, y_train):
    """
    Train the selected model.
    """
    if model_name == "Linear Regression":
        model = LinearRegression()
    elif model_name == "Random Forest":
        model = RandomForestRegressor()
    elif model_name == "Gradient Boosting":
        model = GradientBoostingRegressor()
    else:
        st.error("Invalid model name!")
        return None

    model.fit(X_train, y_train)
    save_model(model, model_name)  # Save the model after training
    return model

def run_model_training():
    st.title("Model Training")
    st.markdown("Train different models and evaluate their performance.")

    # Load the processed data (using temporary function)
    df = load_combined_data()
    
    if df is None:
        st.error("Processed data not found. Please run data preprocessing first.")
        return

    # Splitting the dataset into features and target variable
    X = df.drop(columns=["Target"])  # Features
    y = df["Target"]  # Target variable

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # User selects model for training
    model_name = st.selectbox("Select a model for training", ["Linear Regression", "Random Forest", "Gradient Boosting"])

    if st.button("Train Model"):
        # Train the selected model
        model = train_model(model_name, X_train, y_train)
        
        if model:
            # Make predictions
            y_pred = model.predict(X_test)

            # Evaluate the model
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            # Display the results
            st.subheader(f"Performance of {model_name}:")
            st.write(f"Mean Squared Error (MSE): {mse}")
            st.write(f"R-squared: {r2}")

            # Optionally, display predictions vs actual values
            st.subheader("Predictions vs Actual Values")
            predictions_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
            st.dataframe(predictions_df)

# Run the model training function in Streamlit
if __name__ == "__main__":
    run_model_training()

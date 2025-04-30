
import streamlit as st

def app():
    st.title("🌍 Climate Change Impact Assessment in Nepal")
    
    st.markdown("""
    Welcome to the **Climate Change Impact Assessment and Prediction System for Nepal**.

    This project aims to understand and predict the effects of climate change on Nepal's regions by analyzing both climate and socio-economic datasets. The insights generated can help in informed decision-making for sustainable development and climate resilience.

    ---
    ### 🔍 Project Highlights
    - 🌦️ Analysis of historical climate data (temperature, precipitation, humidity, etc.)
    - 📊 Socio-economic factor integration (health, education, energy, etc.)
    - 🤖 Machine Learning models for prediction
    - 📈 Visualization tools to explore trends
    - 💬 Sentiment analysis of climate change-related opinions

    ---
    ### 📁 Project Sections:
    - **EDA:** Visual exploration of data
    - **Feature Engineering:** Transform raw data into model-ready features
    - **Model Training:** Train and tune ML models
    - **Evaluation:** Check performance of models
    - **Prediction:** Use trained model to predict outcomes
    - **Sentiment Analysis (Bonus):** Understand people's opinions on climate change

    ---
    ### 👨‍💻 Developed By:
    *Shahar Bind*  
    Omdena Academy Capstone Project – 2025
    """)

if __name__ == "__main__":
    app()

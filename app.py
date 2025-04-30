import streamlit as st
from pages import Home, Train_Model, Evaluate_Model, Predict_Temperature

st.set_page_config(page_title="Nepal Climate Temp Predictor", layout="wide")

PAGES = {
    "🏠 Home": Home,
    "🧠 Train Model": Train_Model,
    "📊 Evaluate Model": Evaluate_Model,
    "🔮 Predict Temperature": Predict_Temperature
}

st.sidebar.title("📚 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.show()

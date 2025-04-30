import streamlit as st
from data_utils import load_dataset, analyze_input_text

def show():
    st.title("📌 Welcome to Nepal Climate Temperature Predictor")

    st.markdown("""
    This tool helps visualize and predict temperature trends using climate, agriculture, and environment-related data.
    """)

    st.header("🔍 Dataset Preview")
    data = load_dataset()
    st.dataframe(data.head())

    st.header("🧠 NLP Climate Text Analyzer")
    user_input = st.text_area("Describe a climate event or pattern:")
    if user_input:
        result = analyze_input_text(user_input)
        st.write("**Tokens:**", result["tokens"])
        st.write("**POS Tags:**", result["pos_tags"])
        st.write("**Lemmas:**", result["lemmas"])
        st.write("**Named Entities:**", result["entities"])

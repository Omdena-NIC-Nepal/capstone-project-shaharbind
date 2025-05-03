import streamlit as st

# Set page config
st.set_page_config(
    page_title="Climate Change Impact Assessment - Nepal",
    page_icon="🌍",
    layout="wide"
)

# Custom header with icons and flag
st.markdown("""
    <div style="background-color:#e6f2ff; padding:20px; border-radius:10px;">
        <h2 style="text-align:center; color:#004080;">
        🌍 Climate Change Impact Assessment in Nepal
        </h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("""---""")

# Project Introduction
st.markdown("""  
This project analyzes climate trends and socio-economic factors to assess and predict the impacts of climate change in Nepal.

---
### 🔍 Project Highlights
- 🌦️ Historical climate data analysis (temperature, rainfall, humidity)
- 📊 Socio-economic factor integration (education, health, energy)
- 🤖 Machine Learning-based predictions
- 📈 Interactive visualizations
- 💬 Climate sentiment analysis (bonus)

---
### 📁 Project Sections:
- **EDA:** Explore and visualize datasets
- **Feature Engineering:** Prepare data for modeling
- **Model Training:** Build predictive models
- **Evaluation:** Assess model accuracy
- **Prediction:** Predict outcomes with final model
- **Sentiment Analysis (optional):** Analyze climate opinions

---
### 👨‍💻 Developed By:
**Arbind Shah**  
Omdena Academy Capstone Project – 2025
""")


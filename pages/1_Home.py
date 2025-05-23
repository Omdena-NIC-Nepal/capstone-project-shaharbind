import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Climate Impact in Nepal",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- MAIN HEADER ----------
st.markdown(
    """
    <div style='background-color: #e6f2ff; padding: 20px; border-radius: 10px; text-align: center;'>
        <h1 style='color: #003366;'>🌍 Climate Change Impact Assessment in <span style="color:#007acc">Nepal</span></h1>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- CALL TO ACTION ----------
st.markdown(
    """
    <div style='margin-top: 20px; background-color: #003366; padding: 15px; border-radius: 8px;'>
        
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- INTRODUCTION ----------
st.markdown("### 📝 Project Introduction")
st.markdown(
    """
    This project analyzes **climate trends** and **socio-economic factors** to assess and predict the impacts of climate change across Nepal's regions.
    """
)

# ---------- HIGHLIGHTS ----------
st.markdown("### 🔍 Project Highlights")
st.markdown(
    """
    - 🌡️ Historical climate data analysis (temperature, rainfall, humidity)
    - 🧮 Socio-economic factor integration (education, health, energy)
    - 📊 Feature engineering and data transformation
    - 🤖 Model training and evaluation
    - 📈 Impact prediction and interpretation
    """
)

# ---------- CONTACT ----------
st.markdown("---")
st.markdown("### 📬 Contact")
st.markdown(
    """
 🔗 Github : [View Project Repository](https://github.com/Omdena-NIC-Nepal/capstone-project-shaharbind)  

    📬 Contact : arbindshah123@gmail.com

    <a href='https://www.linkedin.com/in/arbind-shah' target='_blank'>
        <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='17' style='margin-right:10px;'>Connect with me on LinkedIn
    </a>
    """,
    unsafe_allow_html=True
)



```markdown
# 🌡️ Climate Change Impact Assessment and Prediction System – Nepal

## 📑 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Directory Structure](#directory-structure)
---

## 📘 Project Overview

This project is a Streamlit-based web app for analyzing climate and socio-economic data to predict average maximum temperature in Nepal. It covers:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- ML Model Training & Evaluation
- Climate Prediction Interface
- NLP Sentiment Analysis of climate-related text

🎯 **Target Variable**: `avg_max_temp`

---

## 🚀 Features

- 📊 Interactive EDA with charts & maps  
- 🛠️ Feature selection and processing  
- 🤖 Train multiple ML models (Random Forest, Linear, Ridge)  
- 📈 Evaluate model performance  
- 🔮 Predict climate temperature based on user input  
- 🧠 NLP analysis of climate articles using spaCy  

---

### 📥 Steps:

1. Clone the project:
   ```bash
   git clone https://github.com/YOUR_USERNAME/capstone-project-shaharbind.git
   cd capstone-project-shaharbind
   ```

2. Install all required libraries:
   ```bash
   pip install -r requirements.txt
   ```


---

## 🧑‍💻 Usage

Run the app with:

```bash
streamlit run app.py
```

It will open in your browser at `http://localhost:8501`

### 📌 Navigation:

- **Home**: Intro + NLP sentiment demo  
- **EDA**: Explore raw and combined data  
- **Feature Engineering**: Select useful features  
- **Model Training**: Train machine learning models  
- **Model Evaluation**: Compare trained models  
- **Prediction**: Input data and predict temperature  

---

## 🗂️ Directory Structure

```
capstone-project-shaharbind/
│
├── data/
│   ├── raw/                    # Raw climate & socio-economic datasets
│   ├── processed_data/        # Processed data (combined_data.csv)
│   └── sentiment_data/        # Sentiment text data (positive.csv, negative.csv)
│
├── pages/
│   ├── Home.py
│   ├── EDA.py
│   ├── Feature_Engineering.py
│   ├── Model_Training.py
│   ├── Model_Evaluation.py
│   └── Prediction.py
│
├── app.py                     # Streamlit app entry point
├── data_utils.py              # Helper functions for loading/saving data
├── data_preprocessing.ipynb   # Notebook to preprocess & merge raw data
├── requirements.txt           # List of all dependencies
├── README.txt                 # Project description and basic instructions
├── data_sources.txt           # URLs or sources of the datasets
└── Documentation.md           # This documentation file
```

---

## 🧵 Final Note

- Keep your models, data, and code organized.
- Update this documentation if you make big changes.
- Push to GitHub using `git add .`, `git commit -m "msg"`, `git push`

🎉 **Project complete and documented!**
```
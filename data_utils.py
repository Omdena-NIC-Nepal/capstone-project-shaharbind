# data_utils.py

import pandas as pd
import streamlit as st
import os

@st.cache_data  # Efficient caching of results across reruns (Streamlit v1.14.0+)
def load_combined_data():
    """
    Load the preprocessed combined dataset.
    Returns:
        pd.DataFrame: Processed climate + socio-economic dataset.
    """
    data_path = './data/processed_data/combined_data.csv'
    
    if not os.path.exists(data_path):
        st.error("❌ Processed data file not found. Please run data_preprocessing.ipynb first.")
        return pd.DataFrame()
    
    df = pd.read_csv(data_path)
    return df

@st.cache_data
def load_sentiment_data():
    """
    Load positive and negative sentiment data for NLP tasks.
    Returns:
        (pd.DataFrame, pd.DataFrame): positive and negative sentiment datasets.
    """
    pos_path = './data/sentiment_data/positive.csv'
    neg_path = './data/sentiment_data/negative.csv'

    try:
        pos_df = pd.read_csv(pos_path)
        neg_df = pd.read_csv(neg_path)
        return pos_df, neg_df
    except Exception as e:
        st.warning(f"⚠️ Failed to load sentiment data: {e}")
        return pd.DataFrame(), pd.DataFrame()

def save_combined_data(data, file_path='./data/processed_data/combined_data.csv'):
    """
    Save the processed data to a CSV file.
    Args:
        data (pd.DataFrame): Data to save
        file_path (str): Path where data will be saved (default is './data/processed_data/combined_data.csv')
    """
    data.to_csv(file_path, index=False)
    st.success(f"Data saved to {file_path}")

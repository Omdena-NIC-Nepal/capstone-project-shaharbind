
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_utils import load_combined_data

def run_eda():
    st.title("Exploratory Data Analysis (EDA)")
    st.markdown("This section helps us explore climate and socio-economic trends across Nepal.")

    df = load_combined_data()

    if df is None:
        st.error("Processed data not found. Please run data preprocessing first.")
        return

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Correlation Matrix")
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(plt)

    st.subheader("Trends Over Time")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    time_col = 'Year' if 'Year' in df.columns else df.columns[0]

    feature = st.selectbox("Choose a feature to visualize over time", numeric_cols)

    if feature:
        plt.figure(figsize=(10, 4))
        sns.lineplot(data=df, x=time_col, y=feature)
        plt.title(f"{feature} over time")
        st.pyplot(plt)

# Run in Streamlit
if __name__ == "__main__":
    run_eda()

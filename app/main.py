import sys
from pathlib import Path
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from windrose import WindroseAxes

# Import EDA functions from the provided eda.py logic
from eda import (
    load_data,
    clean_data,
    generate_summary_statistics,
    plot_correlation_heatmap,
    plot_time_series,
    plot_time_series_with_precipitation,
    plot_wind_rose,
    evaluate_cleaning_impact,
    plot_bubble_chart,
)

# Streamlit UI for Dashboard
st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("Exploratory Data Analysis Dashboard")
st.sidebar.header("Upload and Visualization Options")

# Upload CSV file
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    with st.spinner("Loading data..."):
        raw_data = load_data(uploaded_file)

    if not raw_data.empty:
        # Display raw data
        if st.sidebar.checkbox("Show Raw Data"):
            st.subheader("Raw Data")
            st.write(raw_data.head())

        # Clean data
        with st.spinner("Cleaning data..."):
            cleaned_data = clean_data(raw_data)

        if st.sidebar.checkbox("Show Cleaned Data"):
            st.subheader("Cleaned Data")
            st.write(cleaned_data.head())

        # Generate summary statistics
        if st.sidebar.checkbox("Summary Statistics"):
            st.subheader("Summary Statistics")
            summary_stats = generate_summary_statistics(cleaned_data)
            st.dataframe(summary_stats)

        # Plot correlation heatmap
        if st.sidebar.checkbox("Correlation Heatmap"):
            st.subheader("Correlation Heatmap")
            plot_correlation_heatmap(cleaned_data)
            st.pyplot()

        # Time series plot
        if st.sidebar.checkbox("Time Series"):
            column = st.sidebar.selectbox(
                "Select Column for Time Series",
                options=cleaned_data.select_dtypes(include=[np.number]).columns,
            )
            if column:
                st.subheader(f"Time Series: {column}")
                plot_time_series(cleaned_data, column)
                st.pyplot()

        # Time series with precipitation
        if st.sidebar.checkbox("Time Series with Precipitation"):
            st.subheader("Time Series of GHI and Precipitation")
            plot_time_series_with_precipitation(cleaned_data)
            st.pyplot()

        # Wind rose plot
        if st.sidebar.checkbox("Wind Rose"):
            st.subheader("Wind Rose")
            plot_wind_rose(cleaned_data)
            st.pyplot()

        # Evaluate cleaning impact
        if st.sidebar.checkbox("Cleaning Impact Evaluation"):
            st.subheader("Cleaning Impact")
            evaluate_cleaning_impact(cleaned_data)
            st.pyplot()

        # Bubble chart
        if st.sidebar.checkbox("Bubble Chart"):
            st.subheader("Bubble Chart: GHI vs Tamb vs WS")
            plot_bubble_chart(cleaned_data)
            st.pyplot()

else:
    st.info("Please upload a CSV file to proceed.")

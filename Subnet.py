import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function to create a bar chart with the same height
def create_bar_chart(data, labels, title, ylabel):
    fig, ax = plt.subplots(figsize=(10.67, 6))  # 400px height equivalent in inches (assuming 100dpi)
    ax.bar(labels, data, color='skyblue')
    ax.set_facecolor('#212121')
    fig.patch.set_facecolor('#212121')
    ax.set_title(title, color='white')
    ax.set_ylabel(ylabel, color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ax.spines.values():
        spine.set_visible(False)
    return fig

# Function to create a line chart with the same height
def create_line_chart(data1, data2, dates, title, ylabel):
    fig, ax = plt.subplots(figsize=(10.67, 6))  # 400px height equivalent in inches (assuming 100dpi)
    ax.plot(dates, data1, label='Truth', color='red')
    ax.plot(dates, data2, label='Prediction', color='cyan')
    ax.set_facecolor('#212121')
    fig.patch.set_facecolor('#212121')
    ax.set_title(title, color='white')
    ax.set_ylabel(ylabel, color='white')
    ax.tick_params(axis='x', colors='white', rotation=45)
    ax.tick_params(axis='y', colors='white')
    ax.legend()
    for spine in ax.spines.values():
        spine.set_visible(False)
    return fig

# Function to create a bar chart for Miner Meta Data with the same height
def create_miner_meta_chart(data, labels, title):
    fig, ax = plt.subplots(figsize=(10.67, 6))  # 400px height equivalent in inches (assuming 100dpi)
    ax.bar(labels, data, color='green')
    ax.set_facecolor('#212121')
    fig.patch.set_facecolor('#212121')
    ax.set_title(title, color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ax.spines.values():
        spine.set_visible(False)
    return fig

# Sample data for charts
miner_ids = ['Miner1', 'Miner2', 'Miner3', 'Miner4', 'Miner5']
trust_values = [0.9, 0.7, 0.5, 0.3, 0.1]
emission_values = [100, 150, 80, 120, 60]
dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
truth_values = [10, 20, 30, 40, 50]
prediction_values = [12, 18, 28, 45, 55]
meta_data_labels = ['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10']
meta_data_values = [0.8, 0.6, 0.9, 0.3, 0.7, 0.5, 0.4, 0.2, 0.1, 0.3]

# Page setup
st.set_page_config(page_title="User Dashboard", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #212121;
            color: white;
        }
        .block-container {
            margin-left: 20%;
            margin-right: 20%;
        }
        .stSelectbox>div>div {
            width: auto !important;
        }
        .stSelectbox>div>div>div {
            padding: 0.25rem 0.5rem !important;
        }
        [data-baseweb="select"] {
            background: none;
            padding: 0;
        }
        [data-baseweb="select"] > div:before {
            background-color: #90EE90;
        }
        .chart-container {
            height: 500px;
        }
    </style>
    """, unsafe_allow_html=True)

# Dropdown for navigation
page = st.selectbox("Navigation", ["Dashboard", "Send Request"])

if page == "Dashboard":
    st.title("User Dashboard")

    st.markdown("### Subnet News")
    st.markdown("""
        <div style="background-color: #333333; padding: 20px; border-radius: 10px; text-align: center;">
            <h2 style="color: white;">Hello World!</h2>
        </div>
        """, unsafe_allow_html=True)

    # First two charts in the same row
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Miner Trust")
        fig1 = create_bar_chart(trust_values, miner_ids, "Miner Trust", "Trust (0-1)")
        st.pyplot(fig1, use_container_width=True)
    with col2:
        st.markdown("### Total Emission")
        fig2 = create_bar_chart(emission_values, miner_ids, "Total Emission", "Emission")
        st.pyplot(fig2, use_container_width=True)

    # Next two charts with the same height
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### Miner")
        fig3 = create_line_chart(truth_values, prediction_values, dates, "Miner", "Request")
        st.pyplot(fig3, use_container_width=True)
    with col4:
        st.markdown("### Miner Meta Data")
        fig4 = create_miner_meta_chart(meta_data_values, meta_data_labels, "Miner Meta Data")
        st.pyplot(fig4, use_container_width=True)

elif page == "Send Request":
    st.title("Send Request")

    # File upload widget
    uploaded_file = st.file_uploader("Choose a file", type=None)
    if uploaded_file is not None:
        st.write("Filename:", uploaded_file.name)
        st.write("File type:", uploaded_file.type)
        st.write("File size:", uploaded_file.size, "bytes")

    # Text area for request details
    request_details = st.text_area("Request details")

    # Display a button to submit the request
    if st.button("Submit Request"):
        if uploaded_file is not None:
            st.write("Request sent!")

import streamlit as st
import pandas as pd
import numpy as np

# App configuration
st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Predictive Maintenance Dashboard")
st.markdown("""
Welcome to the Predictive Maintenance application! This app demonstrates 
machine learning capabilities for predicting equipment failures.
""")

# Simple demo functionality
st.header("Demo Interface")

# Sample data generation
if st.button("Generate Sample Data"):
    sample_data = pd.DataFrame({
        'Machine_ID': range(1, 101),
        'Temperature': np.random.normal(70, 10, 100),
        'Pressure': np.random.normal(100, 15, 100),
        'Vibration': np.random.normal(5, 2, 100),
        'Status': np.random.choice(['Normal', 'Warning', 'Critical'], 100, p=[0.8, 0.15, 0.05])
    })
    st.dataframe(sample_data)
    
    # Basic statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Machines", 100)
    with col2:
        st.metric("Normal", len(sample_data[sample_data['Status'] == 'Normal']))
    with col3:
        st.metric("Needs Attention", len(sample_data[sample_data['Status'] != 'Normal']))

st.info("""
🔍 **Note**: This is a demonstration application. 
In a production environment, this would connect to real sensor data 
and use trained machine learning models for predictions.
""")

# Footer
st.markdown("---")
st.markdown("Deployed via GitHub Actions CI/CD | Built with Streamlit")

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from huggingface_hub import hf_hub_download
import os

# App title and description
st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Predictive Maintenance Dashboard")
st.markdown("""
This application predicts machine failure based on sensor data.
Upload your sensor data or use the sample data to get predictions.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Upload", "Predictions", "About"])

if page == "Home":
    st.header("Welcome to Predictive Maintenance")
    st.markdown("""
    ### How to use:
    1. Go to **Data Upload** to upload your sensor data
    2. Visit **Predictions** to get failure predictions
    3. Monitor machine health in real-time
    
    ### Features:
    - 📊 Data visualization and analysis
    - 🤖 Machine learning predictions
    - 📈 Performance monitoring
    - 🔔 Alert system for potential failures
    """)
    
    # Sample data preview
    if st.checkbox("Show sample data structure"):
        sample_data = pd.DataFrame({
            'temperature': np.random.normal(70, 10, 100),
            'pressure': np.random.normal(100, 15, 100),
            'vibration': np.random.normal(5, 2, 100),
            'rpm': np.random.normal(3000, 500, 100),
            'failure': np.random.choice([0, 1], 100, p=[0.85, 0.15])
        })
        st.dataframe(sample_data.head(10))
        st.metric("Sample Dataset Size", f"{len(sample_data)} rows")

elif page == "Data Upload":
    st.header("📁 Upload Sensor Data")
    
    uploaded_file = st.file_uploader(
        "Choose a CSV file with sensor data", 
        type="csv",
        help="Upload CSV with columns: temperature, pressure, vibration, rpm"
    )
    
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Data Preview")
                st.dataframe(data.head())
                
            with col2:
                st.subheader("Data Info")
                st.write(f"**Shape:** {data.shape}")
                st.write(f"**Columns:** {list(data.columns)}")
                
        except Exception as e:
            st.error(f"Error reading file: {e}")

elif page == "Predictions":
    st.header("🤖 Failure Predictions")
    
    st.info("""
    ⚠️ Note: This is a demo application. 
    For a real implementation, you would:
    1. Load your trained model
    2. Preprocess the input data
    3. Make predictions
    4. Display results with confidence scores
    """)
    
    # Simulated prediction interface
    st.subheader("Manual Input")
    
    col1, col2 = st.columns(2)
    
    with col1:
        temperature = st.slider("Temperature (°C)", 0, 100, 70)
        pressure = st.slider("Pressure (psi)", 50, 150, 100)
        
    with col2:
        vibration = st.slider("Vibration (mm/s)", 0, 20, 5)
        rpm = st.slider("RPM", 1000, 5000, 3000)
    
    if st.button("Predict Failure Probability"):
        # Simulate prediction (replace with actual model)
        import random
        failure_prob = random.uniform(0, 1)
        
        st.subheader("Prediction Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Failure Probability", f"{failure_prob:.2%}")
            
        with col2:
            status = "⚠️ WARNING" if failure_prob > 0.7 else "✅ NORMAL"
            st.metric("Status", status)
            
        with col3:
            recommendation = "Schedule Maintenance" if failure_prob > 0.7 else "Continue Monitoring"
            st.metric("Recommendation", recommendation)
        
        # Progress bar for probability
        st.progress(float(failure_prob))
        
        if failure_prob > 0.7:
            st.error("🚨 High probability of failure detected! Schedule maintenance immediately.")
        elif failure_prob > 0.3:
            st.warning("⚠️ Moderate failure probability. Monitor closely.")
        else:
            st.success("✅ Low failure probability. System operating normally.")

elif page == "About":
    st.header("About This App")
    st.markdown("""
    ### Predictive Maintenance Application
    
    **Purpose:** 
    This application demonstrates predictive maintenance capabilities using machine learning.
    
    **Technology Stack:**
    - Frontend: Streamlit
    - Backend: Python
    - Deployment: Hugging Face Spaces + GitHub Actions CI/CD
    - Machine Learning: Scikit-learn models
    
    **Features:**
    - Real-time sensor data monitoring
    - Failure prediction algorithms
    - Automated alert system
    - Data visualization dashboard
    
    **Development:**
    - CI/CD pipeline with GitHub Actions
    - Automated deployment to Hugging Face
    - Code quality checks and testing
    """)
    
    st.success("This app is automatically deployed via GitHub Actions CI/CD!")

# Footer
st.markdown("---")
st.markdown("Built with using Streamlit | Deployed via GitHub Actions CI/CD")

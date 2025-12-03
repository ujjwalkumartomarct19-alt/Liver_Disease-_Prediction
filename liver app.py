import streamlit as st
import numpy as np
import pickle


# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Liver Disease Stage Predictor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------
# CUSTOM CSS FOR BEAUTIFUL UI
# ------------------------------------------------------
st.markdown("""
 <style>
    .main-title {
        background: linear-gradient(to right, #4b79a1, #283e51);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 25px;
    }
    .sub-header {
        font-size: 22px;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 15px;
    }
    .prediction-box {
        padding: 25px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        margin-top: 60px;
        text-align: center;
        font-size: 14px;
        color: gray;
    }
 </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------
st.sidebar.title("🩺 Liver Disease Predictor")
st.sidebar.info(
    "This AI-powered tool predicts **five stages** of liver disease:\n"
    "- No Disease\n"
    "- Suspect Disease\n"
    "- Hepatitis\n"
    "- Fibrosis\n"
    "- Cirrhosis"
)
st.sidebar.write("---")
st.sidebar.subheader("📊 Normal Range (Min–Max) Based on Dataset")

# NORMAL RANGE BOXES – FROM YOUR CSV FILE
st.sidebar.markdown("""
<div class='range-box'>
<b>Age:</b> 19 – 77<br>
<b>Albumin:</b> 14.9 – 82.2<br>
<b>Alkaline Phosphatase:</b> 11.3 – 416.6<br>
<b>ALT (Alanine Aminotransferase):</b> 0.9 – 325.3<br>
<b>AST (Aspartate Aminotransferase):</b> 10.6 – 324.0<br>
<b>Bilirubin:</b> 0.8 – 254.0<br>
<b>Cholinesterase:</b> 1.42 – 16.41<br>
<b>Cholesterol:</b> 1.43 – 9.67<br>
<b>Creatinine:</b> 8.0 – 1079.1<br>
<b>Gamma GT:</b> 4.5 – 650.9<br>
</div>
""", unsafe_allow_html=True)


st.sidebar.write("---")
st.sidebar.write("Made with ❤️ **Project Group 4**")

# ------------------------------------------------------
# MAIN TITLE
# ------------------------------------------------------
st.markdown("<div class='main-title'>Liver Disease Stage Prediction</div>", unsafe_allow_html=True)

st.write("### Provide the patient's test details below:")

# ------------------------------------------------------

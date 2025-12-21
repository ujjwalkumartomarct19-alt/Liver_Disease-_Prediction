import streamlit as st
import numpy as np
import pickle
from PIL import Image
import base64

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🫀",
    layout="centered"
)

# -------------------- BACKGROUND IMAGE --------------------
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://www.everydayhealth.com/digestive-health/liver-what-it-is-and-how-it-functions/");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# -------------------- LOAD MODEL --------------------
model = pickle.load(open("liver_model.pkl", "rb"))

# Load scaler if used
try:
    scaler = pickle.load(open("scaler.pkl", "rb"))
    use_scaler = True
except:
    use_scaler = False

# -------------------- TITLE --------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#8B0000;'>🫀 Liver Disease Prediction App</h1>
    <h4 style='text-align:center; color:#333;'>ML-powered health risk analysis</h4>
    """,
    unsafe_allow_html=True
)

st.write("---")

# -------------------- USER INPUT --------------------
st.subheader("🔍 Enter Patient Details")

age = st.slider("Age", 1, 100, 30)
gender = st.selectbox("Gender", ("Male", "Female"))
total_bilirubin = st.number_input("Total Bilirubin", 0.0, 50.0, 1.0)
direct_bilirubin = st.number_input("Direct Bilirubin", 0.0, 20.0, 0.5)
alkphos = st.number_input("Alkaline Phosphotase", 10, 300, 100)
sgpt = st.number_input("Alamine Aminotransferase (SGPT)", 5, 200, 35)
sgot = st.number_input("Aspartate Aminotransferase (SGOT)", 5, 200, 40)
total_proteins = st.number_input("Total Proteins", 2.0, 10.0, 6.5)
albumin = st.number_input("Albumin", 1.0, 6.0, 3.2)
ag_ratio = st.number_input("Albumin and Globulin Ratio", 0.1, 3.0, 1.0)

gender_val = 1 if gender == "Male" else 0

input_data = np.array([[
    age,
    gender_val,
    total_bilirubin,
    direct_bilirubin,
    alkphos,
    sgpt,
    sgot,
    total_proteins,
    albumin,
    ag_ratio
]])

if use_scaler:
    input_data = scaler.transform(input_data)

# -------------------- PREDICTION --------------------
st.write("")
if st.button("🧪 Predict Liver Condition"):
    prediction = model.predict(input_data)

    st.write("")

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Liver Disease Detected")
        st.markdown(
            "<p style='color:red; font-size:18px;'>Please consult a medical professional.</p>",
            unsafe_allow_html=True
        )
    else:
        st.success("✅ No Significant Liver Disease Detected")
        st.markdown(
            "<p style='color:green; font-size:18px;'>Your liver parameters look normal.</p>",
            unsafe_allow_html=True
        )

# -------------------- FOOTER --------------------
st.write("---")
st.markdown(
    """
    <p style='text-align:center; font-size:14px;'>
    Built with ❤️ using Machine Learning & Streamlit <br>
    <b>By Motu</b>
    </p>
    """,
    unsafe_allow_html=True
)





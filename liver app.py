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
# INPUT FORM LAYOUT
# ------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    albumin = st.number_input("Albumin", min_value=0.0, value=3.5)
    alkaline_phosphatase = st.number_input("Alkaline Phosphatase", min_value=0.0, value=200.0)
    alanine_aminotransferase = st.number_input("Alanine Aminotransferase", min_value=0.0, value=30.0)
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0.0, value=30.0)

with col2:
    bilirubin = st.number_input("Bilirubin", min_value=0.0, value=1.0)
    cholinesterase = st.number_input("Cholinesterase", min_value=0.0, value=6.0)
    cholesterol = st.number_input("Cholesterol", min_value=0.0, value=200.0)
    creatinina = st.number_input("Creatinine", min_value=0.0, value=1.0)
    gamma_gt = st.number_input("Gamma Glutamyl Transferase", min_value=0.0, value=30.0)
    protein = st.number_input("Protein", min_value=0.0, value=7.0)

# ------------------------------------------------------
features = np.array([[age, sex, albumin, alkaline_phosphatase,
                      alanine_aminotransferase, aspartate_aminotransferase,
                      bilirubin, cholinesterase, cholesterol, creatinina,
                      gamma_gt, protein]])

features_scaled = scaler.transform(features)
predict_btn = st.button("🔍 Predict Stage", use_container_width=True)

# ------------------------------------------------------
# DISPLAY RESULT BEAUTIFULLY
# ------------------------------------------------------
if predict_btn:
    pred_class = model.predict(features_scaled)[0]
    stage = le.inverse_transform([pred_class])[0]

    # Color-coded box
    color_map = {
        "no disease": "#27ae60",
        "suspect disease": "#f1c40f",
        "hepatitis": "#e67e22",
        "fibrosis": "#d35400",
        "cirrhosis": "#c0392b"
    }

    box_color = color_map.get(stage.lower(), "#3498db")

    st.markdown(
        f"""
        <div class='prediction-box' style='background-color: {box_color}; color: white;'>
            Predicted Stage: <b>{stage.upper()}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# FOOTER
# ------------------------------------------------------
st.markdown(
    "<div class='footer'>© 2025 Liver Disease Predictor | Powered by Machine Learning</div>",
    unsafe_allow_html=True
)


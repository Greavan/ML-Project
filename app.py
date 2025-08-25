import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title("📊 Student Performance Prediction App")

st.write("Enter the details below to predict student performance:")

# Input form
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.selectbox(
        "Race/Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"]
    )
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100, step=1)
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, step=1)

    submitted = st.form_submit_button("Predict")

if submitted:
    try:
        # Create input data
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        st.write("### 🔍 Input Data")
        st.dataframe(pred_df)

        # Prediction
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        st.success(f"🎯 Predicted math Score: **{result[0]}**")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

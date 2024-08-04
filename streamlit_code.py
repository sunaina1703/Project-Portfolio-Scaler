import streamlit as st
import pickle
import numpy as np
import joblib


# Load the pre-trained model
model = joblib.load('final_insurance_prediction_model.pkl')

# Function to make predictions
def predict_premium(inputs):
    inputs = np.array(inputs).reshape(1, -1)
    prediction = model.predict(inputs)
    return prediction[0]

# Streamlit UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #C8E6C9;  /* Pastel Green Background */
        color: #4B2E2A;  /* Dark Brown Text */
    }
    .stTitle, .stHeader, .stSubheader, .stText, .stNumberInput, .stSelectbox, .stTextInput {
        color: #4B2E2A;  /* Dark Brown Text */
    }
    .stButton > button {
        background-color: #A5D6A7;  /* Lighter Pastel Green */
        color: #4B2E2A;  /* Dark Brown Text */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #81C784;  /* Slightly darker green on hover */
    }
    .output-text {
        font-weight: bold;
        font-size: 24px;  /* Larger font size */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Insurance Premium Price Prediction')

st.write('Please provide the following details to predict the premium price:')

age = st.number_input('Age', min_value=0, max_value=100, value=25)
diabetes = st.selectbox('Diabetes', [0, 1])
blood_pressure_problems = st.selectbox('BloodPressureProblems', [0, 1])
any_transplants = st.selectbox('AnyTransplants', [0, 1])
any_chronic_diseases = st.selectbox('AnyChronicDiseases', [0, 1])
height = st.number_input('Height (in cm)', min_value=50, max_value=250, value=170)
weight = st.number_input('Weight (in kg)', min_value=10, max_value=200, value=70)
known_allergies = st.selectbox('KnownAllergies', [0, 1])
history_of_cancer_in_family = st.selectbox('HistoryOfCancerInFamily', [0, 1])
number_of_major_surgeries = st.number_input('NumberOfMajorSurgeries', min_value=0, max_value=4, value=0)

if st.button('Predict Premium Price'):
    inputs = [age, diabetes, blood_pressure_problems, any_transplants, any_chronic_diseases, height, weight, known_allergies, history_of_cancer_in_family, number_of_major_surgeries]
    predicted_price = predict_premium(inputs)
    st.success(f'The predicted premium price is: {predicted_price:.2f}')


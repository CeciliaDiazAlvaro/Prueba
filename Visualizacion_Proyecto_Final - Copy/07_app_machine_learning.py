import streamlit as st
import pickle
import pandas as pd
import joblib
import os

my_path = os.path.abspath('')
# Extract the path where the notebook is being executed
ruta_dinamica = os.path.dirname(os.path.dirname(os.path.dirname(my_path)))

# Include the directory  /data
path_object = os.path.join(ruta_dinamica, 'objects')
model_path=os.path.join(path_object,'cardio_logistic_regression_model.pkl')
scaler_path=os.path.join(path_object,'minmax_scaler.pkl')
# Load the logistic regression model
with open(model_path,'rb') as file:
    model = pickle.load(file)

# Load the saved scaler
scaler = joblib.load(scaler_path)

# Streamlit app to predict cardiovascular disease
st.title("Cardiovascular Disease Prediction")

# Input fields
age = st.number_input("Age (in days)", min_value=0, step=1)
height = st.number_input("Height (in cm)", min_value=0, step=1)
weight = st.number_input("Weight (in kg)", min_value=0.0, step=0.1)

gender = st.radio("Gender", options=["Male", "Female"])
gender_value = 1 if gender == "Male" else 2

systolic_bp = st.number_input("Systolic BP", min_value=0, step=1)
diastolic_bp = st.number_input("Diastolic BP", min_value=0, step=1)

cholesterol = st.radio("Cholesterol", options=["Normal", "Above Normal", "Well Above Normal"])
cholesterol_value = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[cholesterol]

glucose = st.radio("Glucose", options=["Normal", "Above Normal", "Well Above Normal"])
glucose_value = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[glucose]

smoke = st.radio("Smoking", options=["Yes", "No"])
smoke_value = 1 if smoke == "Yes" else 0

alcohol = st.radio("Alcohol", options=["Yes", "No"])
alcohol_value = 1 if alcohol == "Yes" else 0

active = st.radio("Physical Activity", options=["Yes", "No"])
active_value = 1 if active == "Yes" else 0


# Function to predict cardiovascular disease
def predict_cardio():
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'age': [age],
        'gender': [gender_value],
        'height': [height],
        'weight': [weight],
        'ap_hi': [systolic_bp],
        'ap_lo': [diastolic_bp],
        'cholesterol': [cholesterol_value],
        'gluc': [glucose_value],
        'smoke': [smoke_value],
        'alco': [alcohol_value],
        'active': [active_value]
    })

    numeric_cols = ["age", "height", "weight", "ap_hi", "ap_lo"]
    input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])

    # Get the prediction from the model
    prediction = model.predict(input_data)

    # Return the result
    if prediction[0] == 1:
        return "Cardiovascular Disease: Yes"
    else:
        return "Cardiovascular Disease: No"


# Prediction button
if st.button("Predict"):
    result = predict_cardio()
    st.write(result)
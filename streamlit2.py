import streamlit as st
import joblib
import numpy as np

model = joblib.load("inclusion_finance_model.pkl")
features = joblib.load("inclusion_finance.pkl")

st.title("Prédiction Inclusion Financière")

inputs = []

for feature in features:
    val = st.number_input(f"{feature}")
    inputs.append(val)

if st.button("Prédire"):
    prediction = model.predict([inputs])
    
    if prediction[0] == 1:
        st.success("Possède un compte bancaire")
    else:
        st.error("Ne possède pas de compte bancaire")
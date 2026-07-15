import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("🎓 Student Performance Prediction")

study = st.number_input("Study Hours",0.0,12.0)
attendance = st.number_input("Attendance (%)",0.0,100.0)
previous = st.number_input("Previous Marks",0.0,100.0)

if st.button("Predict"):

    prediction = model.predict([[study,attendance,previous]])

    st.success(f"Predicted Final Marks: {prediction[0]:.2f}")
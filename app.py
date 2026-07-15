import streamlit as st
import joblib
import pandas as pd

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="AI-Based Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# -------------------- Load Model --------------------
model = joblib.load("model.pkl")

# -------------------- Title --------------------
st.title("🎓 AI-Based Student Performance Prediction System")

st.write("""
This application predicts a student's **final marks** using a Machine Learning
model trained with **Linear Regression**.

Enter the student's details below and click **Predict**.
""")

st.divider()

# -------------------- User Inputs --------------------
study = st.slider("📚 Study Hours per Day", 0, 12, 5)

attendance = st.slider("🏫 Attendance (%)", 0, 100, 80)

previous = st.slider("📝 Previous Marks", 0, 100, 70)

st.metric("Machine Learning Model", "Linear Regression")

# -------------------- Prediction --------------------
if st.button("Predict Final Marks"):

    prediction = model.predict([[study, attendance, previous]])
    predicted_marks = round(prediction[0], 2)

    st.success(f"🎯 Predicted Final Marks: **{predicted_marks}**")

    # Performance Category
    if predicted_marks >= 85:
        st.success("🌟 Performance: Excellent")
    elif predicted_marks >= 60:
        st.warning("👍 Performance: Average")
    else:
        st.error("📚 Performance: Needs Improvement")

    # Display Inputs
    st.subheader("Input Summary")

    df = pd.DataFrame({
        "Feature": [
            "Study Hours",
            "Attendance",
            "Previous Marks",
            "Predicted Marks"
        ],
        "Value": [
            study,
            attendance,
            previous,
            predicted_marks
        ]
    })

    st.table(df)

    # Chart
    st.subheader("Prediction Visualization")

    chart = pd.DataFrame(
        {
            "Values": [
                study,
                attendance,
                previous,
                predicted_marks
            ]
        },
        index=[
            "Study Hours",
            "Attendance",
            "Previous Marks",
            "Predicted Marks"
        ]
    )

    st.bar_chart(chart)

st.divider()

# -------------------- About Model --------------------
with st.expander("📖 About the Machine Learning Model"):

    st.write("""
### Algorithm
**Linear Regression**

### Machine Learning Type
**Supervised Learning**

### Input Features
- Study Hours
- Attendance
- Previous Marks

### Target Variable
- Final Marks

### Libraries Used
- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

### Future Improvements
- Train using a larger real-world dataset.
- Compare multiple machine learning algorithms.
- Add additional features such as assignment scores and participation.
- Deploy with authentication and prediction history.
""")

st.divider()

st.caption("🚀 Built using Python, Scikit-learn, Streamlit, and Machine Learning")
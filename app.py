import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="AI-Based Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# ---------------- Load Files ---------------- #

model = joblib.load("model.pkl")
r2 = joblib.load("r2.pkl")
mae = joblib.load("mae.pkl")
results = pd.read_csv("results.csv")

# ---------------- Title ---------------- #

st.title("🎓 AI-Based Student Performance Prediction System")

st.write("""
Predict a student's **Final Marks** using a Machine Learning model
trained with **Linear Regression**.
""")

st.divider()

# ---------------- User Inputs ---------------- #

study = st.slider(
    "📚 Study Hours",
    min_value=0,
    max_value=12,
    value=5
)

attendance = st.slider(
    "🏫 Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

previous = st.slider(
    "📝 Previous Marks",
    min_value=0,
    max_value=100,
    value=70
)

st.metric("Machine Learning Model", "Linear Regression")

# ---------------- Prediction ---------------- #

if st.button("Predict Final Marks"):

    prediction = model.predict([[study, attendance, previous]])

    predicted_marks = round(prediction[0], 2)

    st.success(f"🎯 Predicted Final Marks : {predicted_marks}")

    # Performance Category

    if predicted_marks >= 85:
        st.success("🌟 Performance : Excellent")

    elif predicted_marks >= 60:
        st.warning("👍 Performance : Average")

    else:
        st.error("📚 Performance : Needs Improvement")

    # Summary Table

    st.subheader("📋 Prediction Summary")

    summary = pd.DataFrame({

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

    st.table(summary)

    # Bar Chart

    st.subheader("📊 Input Visualization")

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
            "Prediction"

        ]

    )

    st.bar_chart(chart)

# ---------------- Model Performance ---------------- #

st.divider()

st.subheader("📈 Model Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.metric("R² Score", f"{r2:.2f}")

with col2:
    st.metric("MAE", f"{mae:.2f}")

# ---------------- Scatter Plot ---------------- #

st.subheader("📉 Actual vs Predicted")

fig, ax = plt.subplots(figsize=(6,6))

ax.scatter(
    results["Actual"],
    results["Predicted"]
)

ax.plot(

    [

        results["Actual"].min(),
        results["Actual"].max()

    ],

    [

        results["Actual"].min(),
        results["Actual"].max()

    ],

    linestyle="--"

)

ax.set_xlabel("Actual Marks")
ax.set_ylabel("Predicted Marks")
ax.set_title("Actual vs Predicted")

st.pyplot(fig)

# ---------------- About Model ---------------- #

st.divider()

with st.expander("📖 About the Machine Learning Model"):

    st.write("""

### Algorithm
Linear Regression

### Machine Learning Type
Supervised Learning

### Features
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
- Matplotlib

### Evaluation Metrics
- R² Score
- Mean Absolute Error (MAE)

### Future Improvements
- Use a larger real-world dataset.
- Compare multiple ML algorithms.
- Feature Engineering.
- Hyperparameter Tuning.
- Deploy with Login System.

""")

st.divider()

st.caption("🚀 Built with Python | Scikit-learn | Streamlit | Machine Learning")
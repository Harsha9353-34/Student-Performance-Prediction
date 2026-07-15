# 🎓 AI-Based Student Performance Prediction System

A Machine Learning web application that predicts a student's final marks based on **Study Hours**, **Attendance**, and **Previous Marks** using **Linear Regression**. The application is built with **Python**, **Scikit-learn**, and **Streamlit**, and is deployed online using Streamlit Community Cloud.

---

## 🚀 Live Demo

🌐 **Live Application:** https://student-performance-prediction-5upm7mf5owxekux7wsrsrf.streamlit.app/

---

## 📌 Project Overview

This project demonstrates the complete Machine Learning workflow:

- Data Collection
- Data Preprocessing
- Model Training
- Model Evaluation
- Prediction
- Deployment

The application allows users to enter student details and instantly predict the expected final marks.

---

## ✨ Features

- 🎯 Predict student final marks
- 📊 Interactive Streamlit dashboard
- 📈 Model evaluation using **R² Score**
- 📉 Mean Absolute Error (MAE)
- 📋 Prediction summary table
- 📊 Input visualization using charts
- 📉 Actual vs Predicted scatter plot
- ☁️ Deployed on Streamlit Cloud

---

## 🧠 Machine Learning

### Algorithm
- Linear Regression

### Machine Learning Type
- Supervised Learning

### Input Features
- Study Hours
- Attendance
- Previous Marks

### Target Variable
- Final Marks

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Git
- GitHub

---

## 📂 Project Structure

```text
Student-Performance-Prediction/
│── app.py
│── train_model.py
│── student_data.csv
│── model.pkl
│── r2.pkl
│── mae.pkl
│── results.csv
│── requirements.txt
└── README.md
```

---

## 📊 Model Evaluation

The model is evaluated using:

- **R² Score**
- **Mean Absolute Error (MAE)**

The application also visualizes the relationship between actual and predicted values using a scatter plot.

---

## ▶️ How to Run Locally

### Clone the repository

```bash
git clone https://github.com/Harsha9353-34/Student-Performance-Prediction.git
```

### Navigate to the project

```bash
cd Student-Performance-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Launch the application

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

- Train on a larger real-world educational dataset.
- Compare multiple machine learning algorithms such as Random Forest and XGBoost.
- Add additional features such as assignment scores, participation, and sleep hours.
- Store prediction history in a database.
- Deploy with authentication and user management.

---

## 👨‍💻 Author

**Harsha R**

B.Tech Computer Science Engineering

Interested in AI/ML, Software Development, and Data Science.

---

⭐ If you found this project useful, consider giving it a star!

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("student_data.csv")

X = data[["StudyHours","Attendance","PreviousMarks"]]
y = data["FinalMarks"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model Trained Successfully!")
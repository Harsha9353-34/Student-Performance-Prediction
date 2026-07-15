import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("student_data.csv")

# Features
X = data[["StudyHours", "Attendance", "PreviousMarks"]]

# Target
y = data["FinalMarks"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()

model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Evaluation Metrics
# -----------------------------
r2 = r2_score(y_test, predictions)

mae = mean_absolute_error(y_test, predictions)

# -----------------------------
# Print Metrics
# -----------------------------
print("=" * 40)
print("MODEL PERFORMANCE")
print("=" * 40)

print(f"R² Score : {r2:.2f}")
print(f"MAE      : {mae:.2f}")

print("=" * 40)

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "model.pkl")

# Save Metrics
joblib.dump(r2, "r2.pkl")
joblib.dump(mae, "mae.pkl")

# -----------------------------
# Save Actual vs Predicted
# -----------------------------
results = pd.DataFrame({

    "Actual": y_test.values,

    "Predicted": predictions

})

results.to_csv("results.csv", index=False)

print("Model Saved Successfully!")
print("Training Completed!")
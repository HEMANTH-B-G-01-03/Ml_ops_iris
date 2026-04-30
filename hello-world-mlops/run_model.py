import joblib

model = joblib.load("artifacts/model.pkl")

sample = [[5.1, 3.5, 1.4, 0.2]]
print("Prediction:", model.predict(sample))
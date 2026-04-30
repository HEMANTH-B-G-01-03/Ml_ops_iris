from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def main():
    X, y = load_iris(return_X_y=True)

    model = RandomForestClassifier()
    model.fit(X, y)

    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/model.pkl")

if __name__ == "__main__":
    main()
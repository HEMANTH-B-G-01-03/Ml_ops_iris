from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
from pathlib import Path

app = Flask(__name__)
CORS(app)

MODEL_PATH = Path("artifacts/model.pkl")

if not MODEL_PATH.exists():
    import train
    train.main()

model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]
    pred = model.predict([features])
    return jsonify({"prediction": int(pred[0])})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
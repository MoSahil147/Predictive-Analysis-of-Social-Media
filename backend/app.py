# app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load models
virality_model = joblib.load("backend/models/virality_model.pkl")
influencer_model = joblib.load("backend/models/influencer_model.pkl")
diffusion_model = joblib.load("backend/models/diffusion_model.pkl")

# Virality Prediction API
@app.route('/predict_virality', methods=['POST'])
def predict_virality():
    data = request.get_json()
    features = [[data['likes'], data['shares'], data['comments']]]
    prediction = virality_model.predict(features)[0]
    return jsonify({"virality_score": prediction})

# Influencer Prediction API
@app.route('/predict_influencer', methods=['POST'])
def predict_influencer():
    data = request.get_json()
    features = [[data['followers'], data['posts'], data['likes'], data['comments'], data['shares'], data['engagement_rate']]]
    prediction = influencer_model.predict(features)[0]
    return jsonify({"is_influencer": bool(prediction)})

# Misinformation Detection API
@app.route('/predict_diffusion', methods=['POST'])
def predict_diffusion():
    data = request.get_json()
    features = [[data['likes'], data['shares'], data['comments'], data['engagement_rate']]]
    prediction = diffusion_model.predict(features)[0]
    return jsonify({"is_misinformation": bool(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

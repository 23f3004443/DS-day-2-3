from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

classes = ['setosa', 'versicolor', 'virginica']

@app.route('/',  methods=["GET"])
def home():
    return jsonify({"messge" : "Model API up and running...."})

@app.route('/predict', methods=["POST"])
def predict():
    data=request.get_json()

    if data is None or "features" not in data:
        return jsonify({"error" : "Data must contain a 'features' field"}), 400

    if not isinstance(data['features'], list) or  len(data['features']) != 4:
        return jsonify({"error" : "Data should be in list format and 4 elements should be present"}), 400

    features=data['features']

    pred=model.predict([features])
    return jsonify({"prediction" : classes[int(pred[0])]})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
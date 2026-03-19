from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]

    sentiment = "Positive 😊" if prediction == 1 else "Negative 😠"

    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)
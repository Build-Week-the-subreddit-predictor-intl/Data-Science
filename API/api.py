from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import pandas as pd

app = Flask(__name__)
CORS(app)
# app.config["DEBUG"] = True

model = load('alg.sav')


@app.route('/', methods=['GET'])
def home():
    return "Go to /input?title=[title text]&body=[body text]"


@app.route('/input', methods=['POST', 'GET'])
def ask():
    try:
        title = request.args['title']
        body = request.args['body']
    except KeyError:
        return "missing args -- try title= & body="
    # data = {'title': [title], 'selftext': [body]}
    # data = {'selftext': [body]}
    # df = pd.DataFrame(data=data)
    body = [body]
    result = model.predict(body)
    return jsonify({'subreddit': result[0]})

# app.run()
# or run with gunicorn api:app

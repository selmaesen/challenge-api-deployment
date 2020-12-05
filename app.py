import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from pipeline.predict import prediction
import pipeline.model as model

app = Flask(__name__)


@app.route("/")
def home():
    """
    function returns string on home page
    parameters: GET
    return: "Welcome to API Deployment"
    """
    return "Welcome to API Deployment"


@app.route('/welcome')
def welcome():
    """
    function returns string on welcome page
    parameters: GET
    return: "Alive!"
    """
    return "Alive!"


@app.route("/predict", methods=["POST", "GET"])
def predict():
    """
    function returns predicted price
    parameters: GET,POST
    return: "The predicted price is VALUE"
    """
    data = request.get_json()
    dataset = pd.DataFrame([data])
    result = prediction.predict(dataset)

    return jsonify(("The predicted price is {}".format(result)))


if __name__ == '__main__':
    # run app on port 5000
    app.run(host="0.0.0.0", port=5000)

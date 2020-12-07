import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from pipeline.predict.prediction import predict
from pipeline.preprocessing.cleaning_data_vers02 import preprocess
import pipeline.model as model

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    function returns string on welcome page
    parameters: GET
    return: "Alive!"
    """
    return "Alive!"


@app.route('/welcome', methods=["GET"])
def welcome():
    """
    function returns string on home page
    parameters: GET
    return: "Welcome to API Deployment"
    """
    return "Welcome to API Deployment"


@app.route("/predict", methods=["POST"])
def predict_api():
    """
    function returns predicted price
    parameters: GET,POST
    return: "The predicted price is VALUE"
    """
    data = request.get_json()
    dataset = pd.DataFrame(data, index=[0, ])
    new_df = preprocess(dataset)

    print(type(new_df))
    if isinstance(new_df, str):

        return "Error!"
    else:

        result = predict(new_df)
        return jsonify(result)


if __name__ == '__main__':
    app.run(post=5000,host='0.0.0.0')

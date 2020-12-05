import numpy as np
import flask from Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('houseprice_model.pkl', 'rb'))

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/predict", methods = [POST])
def predict()
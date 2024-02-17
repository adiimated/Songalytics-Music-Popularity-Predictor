from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle
from model_prep import (
    load_model,
    acoustic_features,
    get_graph_data
)

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/landing")
def landing():
    return render_template("landing2.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        csv_file = request.files['csv_file']
        org_data = pd.read_csv(csv_file, sep="\t", index_col=0)
        
        # org_data = org_data.set_index('org_index')

        predictions = make_prediction(org_data)

        org_data["predictions"] = predictions

        # TODO add the categorical values as well

        json_list = get_json_data(org_data)

        # send this with the template
        return render_template('results.html', data=json_list)

@app.route("/graph_data")
def graph_data():
    songs_df = pd.read_csv("phase2_data.csv", sep="\t")
    res = get_graph_data(songs_df)
    return jsonify(res)


def get_json_data(data: pd.DataFrame):
    cols = acoustic_features + ["predictions"]
    json_list = data[cols].sort_values(by="predictions", ascending=False).to_dict(orient="records")
    return json_list


def make_prediction(data):

    # TODO get the form data's columns
    #  in the right order if not in the right order

    # Process the form data, transform it to match the input of the model
    X_test = data

    print(X_test.head())
    # load the model
    model = load_model()

    # Make predictions using the trained model
    prediction = model.predict(X_test)
    # Return the prediction
    return prediction


if __name__ == "__main__":
    app.run(debug=True)
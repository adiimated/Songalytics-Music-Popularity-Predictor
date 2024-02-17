from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load and preprocess the dataset
# Replace the path below with the actual path to your dataset
dataset_path = "phase2_data.csv"

categorical_columns = [
    'song_type',
    'artist_type',
    'main_genre'
]

acoustic_categorical_columns = [
    'key',
    'mode',
    'time_signature'
]

acoustic_features = [
    'duration_ms',
    'acousticness',
    'danceability',
    'energy',
    'instrumentalness',
    'liveness',
    'loudness',
    'speechiness',
    'valence',
    'tempo'
]

predict_col = "rank_score"


def get_data_from_csv(filename="phase2_data.csv"):
    # read the data from the csv and return the dataframe
    data: pd.DataFrame = pd.read_csv(filename, index_col=0, sep="\t")
    return data

def save_test_data(data: pd.DataFrame):
    X_train, X_test = train_test_split(
        data, test_size=0.3, random_state=42, stratify=data[categorical_columns + acoustic_categorical_columns]
    )
    X_test.to_csv("testing_upload.csv", sep="\t")

def get_train_test_set(data: pd.DataFrame):

    data = data[categorical_columns + acoustic_categorical_columns + acoustic_features + [predict_col]]

    X = data.drop(predict_col, axis=1)
    X = encode_data(X)
    y = [1 if i >= 66.5 else 0 for i in data[predict_col]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    X_test.to_csv("testing_data.csv", sep="\t")

    return X_train, X_test, y_train, y_test


def encode_data(songs_df: pd.DataFrame):

    # Load data
    data = songs_df[ acoustic_categorical_columns + acoustic_features + [predict_col]]
    data["rank_score"]= [ 1 if i >=50 else 0 for i in data.rank_score]

    # Encode categorical columns using label encoding
    le = LabelEncoder()

    for col in acoustic_categorical_columns :
        data[col] = le.fit_transform(data[col])

    data = pd.get_dummies(data, columns=acoustic_categorical_columns)

    # Standardize numeric columns
    scaler = StandardScaler()
    data[acoustic_features] = scaler.fit_transform(data[acoustic_features])

    X = data.drop(predict_col, axis=1)
    y = data[predict_col]
    return train_test_split(X, y, test_size=0.3, random_state=42)


def train_model():

    predict_col = "rank_score"
    
    data: pd.DataFrame = get_data_from_csv()

    X_train, X_test, y_train, y_test = encode_data(data)

    X_test.to_csv("testing_data.csv", sep="\t")

    # Train the model
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    # Make predictions on test set and evaluate model
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    print("Saving model to model.pkl file")
    # save the model to a pickle file.
    with open('model.pkl', 'wb') as file:
        pickle.dump(rf, file)


def load_model(filename="model.pkl"):
    # read from the model file and return the model
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    return model

def get_bar_graph(data: pd.DataFrame):
    # PLOTTING BAR CHART DEPICTING COUNT DISTRIBUTION OF POPULARITY OF SONGS
    res = data.is_pop_song.value_counts().sort_values()
    return res.to_dict()

def get_line_graph(songs_df: pd.DataFrame):

    # EDA -- SONG COUNT OVER THE YEARS -- TREND
    line1 = songs_df[["song_id", "year"]].groupby(["year"]).count()
    total = line1.to_dict()["song_id"]

    # EDA -- EXPLICIT SONG COUNT OVER THE YEARS -- TREND
    line2 = songs_df[songs_df["explicit"] == True][["song_id", "year"]].groupby(["year"]).count()
    explicit = line2.to_dict()["song_id"]

    # EDA -- NON EXPLICIT OVER THE YEARS -- TREND
    line3 = songs_df[songs_df["explicit"] == False][["song_id", "year"]].groupby(["year"]).count()
    non_explicit = line3.to_dict()["song_id"]

    res = {
        "total": total,
        "explicit": explicit,
        "non_explicit": non_explicit
    }

    return res


def get_radar_chart(data: pd.DataFrame):

    # top hundred songs mean of acoustic features
    hun_mean = data.sort_values(by=["year_end_score"], ascending=False)[
        [
            'mode',
            'acousticness',
            'danceability',
            'energy',
            'instrumentalness',
            'liveness',
            'speechiness',
            'valence'
        ]
    ].iloc[:100].mean()


    sorted_mean = data[
        [
            'mode',
            'acousticness',
            'danceability',
            'energy',
            'instrumentalness',
            'liveness',
            'speechiness',
            'valence'
        ]
    ].mean()

    labels = list(hun_mean.index)
    features = hun_mean.tolist()
    features_all = sorted_mean.tolist()

    res = {
        "labels": labels,
        "features": features,
        "features_all": features_all
    }

    return res

def get_graph_data(data: pd.DataFrame):

    res = {
        "bar_graph": get_bar_graph(data),
        "line_graph": get_line_graph(data),
        "radar_graph": get_radar_chart(data)
    }
    
    return res
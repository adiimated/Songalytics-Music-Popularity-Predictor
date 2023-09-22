# Songalytics: Spotify Data Analytics

## Introduction

## Dataset

The dataset I used is a comprehensive compilation of Spotify tracks across 125 different genres, stored in a tabular CSV format. It offers a broad spectrum of audio features and metadata for each track, including the track's ID, artists, album name, popularity score, duration, explicitness, and numerous audio properties like danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, and time signature.

Link : https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

## Cleaning the data set

Steps taken to clean the data:
1. Dropping irrelevant columns - Unnamed, track_id
2. Identifying columns with missing values and dropping null values
3. Checking for duplicate rows and dropping them
4. Checking the data type of columns - changing if required
5. Removing Outliers
6. Created a new column based  on popularity score - popularity category : Based on the popularity score, a new categorical column named ‘popularity category’ was created. The scores were divided into four categories: ‘emerging’ (0-25), ‘upandcoming’ (26-50), ‘mainstreamhits’ (51-75), and ‘charttoppers’ (76-100). Creating this new column is significant as it facilitates segmented analysis, allowing for a more nuanced understanding of the different popularity levels of the tracks

| Category  | Popularity Score Range |
| ------------- | ------------- |
| Emerging | 0-25 |
| Up and Coming  | 26-50  |
| Mainstream Hits  | 51-75 |
| Chart Toppers  | 76-100  |


## Explorartory Data Analysis

### Summary Statistics

#### Categorical Features:

| Feature | Analysis |
| ------------- | ------------- |
| artists  | There are 30,119 unique artists with "The Beatles" appearing most frequently (271 times).  |
| album_name  | 44,588 unique album names with "Alternative Christmas 2022" being the most frequent album name (185 times)  |
| track_name  | 9,477 unique track names with "Run Rudolph Run" appearing most frequently (151 times).  |
| track_genre  | 114 unique genres with "sad" being the most frequent genre (1,000 times).  |
| popularity_category  | 4 unique categories with "Emerging Artists" being the most frequent category (41,279 times). |

| Content Cell  | Content Cell  |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |


#### Numerical Features:

## What constitutes a popular song ?

## Machine Learning Algos

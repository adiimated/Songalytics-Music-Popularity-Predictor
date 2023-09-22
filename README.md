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

Here are some fun ones!

| Feature | Analysis |
| ------------- | ------------- |
| artists  | There are 30,119 unique artists with "The Beatles" appearing most frequently (271 times).  |
| album_name  | 44,588 unique album names with "Alternative Christmas 2022" being the most frequent album name (185 times)  |
| track_name  | 9,477 unique track names with "Run Rudolph Run" appearing most frequently (151 times).  |
| track_genre  | 114 unique genres with "sad" being the most frequent genre (1,000 times).  |
| popularity_category  | 4 unique categories with "Emerging Artists" being the most frequent category (41,279 times). |

### Distribution of Numerical Features

![Distribution of Numerical Features](https://github.com/adiimated/Songalytics-Spotify-Data-Analysis/blob/main/images/distribution.png)

When interpreting the provided histograms, we are getting insights into the different characteristics of a collection of music tracks. Let’s break down these insights:

Popularity:

    Majority Low Popularity: Most of the tracks have popularity between 0 and 40.
    Some High Popularity: Few tracks exist with high popularity, extending up to 100.

Duration_ms:

    Mainstream Duration: Most tracks have a duration between 100,000 ms (1.67 minutes) and 300,000 ms (5 minutes).
    Extended Duration: Few tracks are longer than the typical range.

Danceability:

    Moderate to High Danceability: The majority of tracks score between 0.4 and 0.8 on danceability, indicating a general preference for danceable music.

Energy:

    Balanced Distribution: Energy levels are evenly distributed, with a slight inclination towards higher energy levels.

Key:

    Uniform Distribution: Tracks are spread across different keys uniformly, indicating a varied musical scale presence.

Loudness:

    Predominantly Loud: The majority of the tracks are loud, falling between -10 and -5 dB, with fewer tracks being quieter.

Speechiness:

    Predominantly Non-Speechy: Most tracks have low speechiness, indicating that they contain more music than spoken words.

Acousticness:

    Varied Acousticness: Many tracks have low to moderate acousticness with fewer tracks having high acousticness.

Instrumentalness:

    Predominantly Non-Instrumental: Most tracks are not instrumental.
    Variety: Few tracks exhibit moderate to high instrumentalness.

Liveness:

    Studio-like Quality: Most tracks have low liveness, meaning they probably are studio recordings with less audience noise.
    Few Live Recordings: Some tracks have high liveness, indicating potential live recordings.

Valence:

    Balanced Mood: Tracks have a balanced distribution in terms of valence with a slight inclination towards happier or more positive music.

Tempo:

    Common Tempo: Most tracks lie in the common tempo range of 80 to 140 BPM (Beats Per Minute).
    Varied Tempo: Few tracks fall outside the common tempo range, suggesting variety in rhythm speed.

Time_Signature:

    Common Time: Most tracks have a 4/4 time signature, which is the most common time signature in modern music.

Conclusion:

This collection seems to contain a diverse range of music tracks but leans more towards mainstream preferences, such as moderate to high danceability, higher energy levels, louder volumes, and common time signatures. There are also instances of less common musical elements, providing a variety, such as tracks with high instrumentalness, varied tempo, and live recordings. The uniform distribution in keys also ensures a wide range of musical scales.


## What constitutes a popular song ?

## Machine Learning Algos

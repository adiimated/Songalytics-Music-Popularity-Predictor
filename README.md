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

a. Artists:
The dataset incorporates a diverse collection of 30,119 unique artists, where "The Beatles" is the preeminent group, featured 271 times, marking the highest frequency among all the artists present.

b. Album Name:
With 44,588 distinct album names present, "Alternative Christmas 2022" emerges as the most prevalent album, being mentioned 185 times, signifying the album's predominant representation.

c. Track Name:
The dataset reveals a comprehensive array of 69,477 unique track names, with "Run Rudolph Run" as the most recurring track, appearing 151 times.

d. Track Genre:
Among the 114 genres, "sad" is recognized as the most prevalent genre, appearing 1,000 times. This dominance can suggest a significant preference or production in this genre.

e. Popularity Category:
There are four distinguished popularity categories, with "Emerging Artists" being the most recurrent, evident 41,279 times, indicating a major portion of the dataset is attributed to new and rising artists.

#### Numerical Features:

a. Popularity:
The popularity score is dispersed between 0 to 100, harboring an average of approximately 33.59, and the central tendency is around 35, implying a moderate popularity level among the tracks.

b. Duration_ms:
The duration of the tracks varies between 43,133 to 392,656 milliseconds, with an average track length of approximately 214,669 milliseconds.

c. Explicit:
The explicit feature is binary, and 75% of the tracks are marked as non-explicit, indicating a dominance of cleaner and more universally adaptable tracks.

d. Danceability, Energy, & Instrumentalness:
These features have values ranging from 0 to 1. The average danceability and energy are 0.569 and 0.643 respectively, suggesting a moderate tendency towards danceable and energetic tracks. The instrumentalness has a low mean of approximately 0.140, indicating a lesser prevalence of instrumental tracks.

e. Key & Loudness:
The key has a range from 0 to 11 with a mean and median around 5.31 and 5, respectively, while the loudness varies extensively from -49.531 to 4.532 dB, with an average value around -8.136 dB.

f. Mode:
Similar to explicit, mode is a binary feature, with 75% of the tracks being in mode 1, reflecting a prevalent usage of this mode.

g. Speechiness, Acousticness, Liveness, & Valence:
With average values of approximately 0.085, 0.317, 0.213, and 0.481 respectively, these features suggest a minimal presence of spoken words, a moderate presence of acoustic sound, a low likelihood of the presence of an audience, and a near-neutral mood within the tracks.

h. Tempo & Time Signature:
The tempo demonstrates variability from 0 to 243.372 BPM, with a mean value close to 122.2 BPM. The time signature oscillates between 0 to 5, predominantly scoring around 4, aligning with the common time in music theory.

## What constitutes a popular song ?

## Machine Learning Algos

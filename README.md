# Songalytics: Spotify Data Analytics [work in progress]

## Introduction

"Unlock the Rhythm of Music: Spotify Data Analysis and Song Popularity Prediction" 🎵

Discover the magic of Spotify data analysis as we unravel the hidden stories behind your favorite tunes. Our project goes beyond the surface, using data science techniques to extract meaningful insights from Spotify's extensive music library. From genre trends to tempo preferences, we explore it all.

But that's not all – we take it a step further! 🚀

Our predictive model doesn't just stop at analysis; it forecasts the future of songs. Want to know which track might become the next chart-topper? Look no further! Our Popularity Prediction algorithm uses data-driven intelligence to provide a glimpse into the future of music.

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

* Majority Low Popularity: Most of the tracks have popularity between 0 and 40.
* Some High Popularity: Few tracks exist with high popularity, extending up to 100.
* Mainstream Duration: Most tracks have a duration between 100,000 ms (1.67 minutes) and 300,000 ms (5 minutes).
* Extended Duration: Few tracks are longer than the typical range.
* Moderate to High Danceability: The majority of tracks score between 0.4 and 0.8 on danceability, indicating a general preference for danceable music.
* Balanced Distribution: Energy levels are evenly distributed, with a slight inclination towards higher energy levels.
* Uniform Distribution: Tracks are spread across different keys uniformly, indicating a varied musical scale presence.
* Predominantly Loud: The majority of the tracks are loud, falling between -10 and -5 dB, with fewer tracks being quieter.
* Predominantly Non-Speechy: Most tracks have low speechiness, indicating that they contain more music than spoken words.
* Varied Acousticness: Many tracks have low to moderate acousticness with fewer tracks having high acousticness.
* Predominantly Non-Instrumental: Most tracks are not instrumental.
* Variety: Few tracks exhibit moderate to high instrumentalness.
* Studio-like Quality: Most tracks have low liveness, meaning they probably are studio recordings with less audience noise.
* Few Live Recordings: Some tracks have high liveness, indicating potential live recordings.
* Balanced Mood: Tracks have a balanced distribution in terms of valence with a slight inclination towards happier or more positive music.
* Common Tempo: Most tracks lie in the common tempo range of 80 to 140 BPM (Beats Per Minute).
* Varied Tempo: Few tracks fall outside the common tempo range, suggesting variety in rhythm speed.
* Common Time: Most tracks have a 4/4 time signature, which is the most common time signature in modern music.

Conclusion:

This collection seems to contain a diverse range of music tracks but leans more towards mainstream preferences, such as moderate to high danceability, higher energy levels, louder volumes, and common time signatures. There are also instances of less common musical elements, providing a variety, such as tracks with high instrumentalness, varied tempo, and live recordings. The uniform distribution in keys also ensures a wide range of musical scales.

### Distribution of Categorical Features

![Distribution of Categorical Features](https://github.com/adiimated/Songalytics-Spotify-Data-Analysis/blob/main/images/Cat%20features.png)

* Explicit: The majority of the tracks are not explicit, with a smaller number of tracks being explicit.
* Mode: Most tracks are in Mode 1, with fewer tracks in Mode 0.
* Track Genre: The dataset has a diverse set of genres, with "sad", "upbeat", and "chill" being the most frequent ones.
* Popularity Category: The majority of the tracks fall under the "Emerging Artists" category, followed by "Mainstream Hits", "Underground Hits", and "Chart-Toppers".

### Correlation Matrix

![](https://github.com/adiimated/Songalytics-Spotify-Data-Analysis/blob/main/images/corr%20matrix.png)

Observations:

* Energy and Loudness have a strong positive correlation of 0.78, which is expected as louder songs are usually perceived as more energetic.
* Valence and Danceability have a moderate positive correlation of 0.54, indicating that tracks perceived as more positive or happier tend to be more danceable.
* Energy and Acousticness have a strong negative correlation of -0.71, suggesting that more energetic songs tend to have lower acousticness.
* Loudness and Acousticness have a moderate negative correlation of -0.56, indicating that louder songs tend to have lower acousticness.
* Energy and Valence have a moderate positive correlation of 0.39, suggesting that more energetic songs tend to be more positive or happier.
* Danceability and Speechiness have a moderate positive correlation of 0.22, indicating that more danceable songs tend to have more spoken words.

###  Box plots for numerical features against popularity_category

![](https://github.com/adiimated/Songalytics-Spotify-Data-Analysis/blob/main/images/box%20plots%20by%20popularity%20category.png)

* Popularity: As expected, "Chart-Toppers" have the highest median popularity, followed by "Mainstream Hits," "Emerging Artists," and "Underground Hits."
* Danceability: "Mainstream Hits" and "Chart-Toppers" tend to have higher median danceability compared to "Emerging Artists" and "Underground Hits."
* Energy: "Chart-Toppers" have a higher median energy level compared to other categories.
* Loudness: "Chart-Toppers" and "Mainstream Hits" tend to be louder compared to "Emerging Artists" and "Underground Hits."

### Top 10 genres based on their frequencies

```
sad            1000
rockabilly      999
rock-n-roll     999
study           998
mandopop        997
electro         997
chill           997
house           997
sertanejo       996
cantopop        996
```

### Artists with most Chart Toppers

![](https://github.com/adiimated/Songalytics-Spotify-Data-Analysis/blob/main/images/Screenshot%202023-09-22%20at%201.36.55%20PM.png)

### Average Dancebility for Top 10 Frequent Genres

## What constitutes a popular song ?

## Machine Learning Algos

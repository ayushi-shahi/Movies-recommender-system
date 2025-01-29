<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>About</h1>
    <p>This Movie Recommendation System suggests movies based on user preferences. It utilizes content-based filtering and cosine similarity to recommend similar movies.</p>

   Features

Content-Based Filtering: Recommends movies similar to the selected one.
Search Functionality: Users can search for any movie.
Machine Learning Model: Uses cosine similarity for recommendations.
Web Interface: Built with Flask for an interactive UI.
Tech Stack

Python (Flask, NumPy, Pandas)
Scikit-Learn (Cosine Similarity)
Pickle (Model Storage)
HTML, CSS, Bootstrap (Frontend)
Heroku Deployment
How It Works

Preprocessing: The dataset is cleaned, and important features are extracted.
Vectorization: Converts text-based features (genres, descriptions) into numerical form using TF-IDF.
Similarity Calculation: Computes cosine similarity to find similar movies.
Recommendation Generation: When a user selects a movie, the system suggests similar ones.

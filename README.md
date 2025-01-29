<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Recommendation System</title>
</head>
<body>
    <h1>About</h1>
    <p>This Movie Recommendation System suggests movies based on user preferences. It utilizes content-based filtering and cosine similarity to recommend similar movies.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Content-Based Filtering:</strong> Recommends movies similar to the selected one.</li>
        <li><strong>Search Functionality:</strong> Users can search for any movie.</li>
        <li><strong>Machine Learning Model:</strong> Uses cosine similarity for recommendations.</li>
        <li><strong>Web Interface:</strong> Built with Flask for an interactive UI.</li>
    </ul>

    <h2>Tech Stack</h2>
    <ul>
        <li>Python (Flask, NumPy, Pandas)</li>
        <li>Scikit-Learn (Cosine Similarity)</li>
        <li>Pickle (Model Storage)</li>
        <li>HTML, CSS, Bootstrap (Frontend)</li>
        <li>Heroku Deployment</li>
    </ul>

    <h2>How It Works</h2>
    <ul>
        <li><strong>Preprocessing:</strong> The dataset is cleaned, and important features are extracted.</li>
        <li><strong>Vectorization:</strong> Converts text-based features (genres, descriptions) into numerical form using TF-IDF.</li>
        <li><strong>Similarity Calculation:</strong> Computes cosine similarity to find similar movies.</li>
        <li><strong>Recommendation Generation:</strong> When a user selects a movie, the system suggests similar ones.</li>
    </ul>
</body>
</html>

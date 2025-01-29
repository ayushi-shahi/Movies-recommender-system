<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Recommendation System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        code {
            background: #f4f4f4;
            padding: 5px;
            border-radius: 5px;
            font-size: 14px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
    </style>
</head>
<body>

<div class="container">
    <h1> Movie Recommendation System</h1>
    <img src="https://miro.medium.com/max/1400/1*9fZltYXqxFeZFYc-94jK1A.png" width="100%" alt="Movie Recommendation System">

    <h2> About</h2>
    <p>
        This <strong>Movie Recommendation System</strong> suggests movies based on user preferences.
        It utilizes machine learning techniques such as <strong>content-based filtering</strong> and 
        <strong>cosine similarity</strong> to recommend movies similar to the one selected by the user.
    </p>

    <h2> Features</h2>
    <ul>
        <li> <strong>Content-Based Filtering</strong>: Recommends movies similar to the selected movie.</li>
        <li> <strong>Search Functionality</strong>: Users can search for any movie.</li>
        <li><strong>Machine Learning Model</strong>: Uses cosine similarity for recommendations.</li>
        <li> <strong>Web Interface</strong>: Built with Flask for an interactive UI.</li>
    </ul>

    <h2>🛠 Tech Stack</h2>
    <ul>
        <li><strong>Python</strong> (Flask, NumPy, Pandas)</li>
        <li><strong>Scikit-Learn</strong> (Cosine Similarity)</li>
        <li><strong>Pickle</strong> (Model Storage)</li>
        <li><strong>HTML, CSS, Bootstrap</strong> (Frontend)</li>
        <li><strong>Heroku Deployment</strong></li>
    </ul>

    <h2> How It Works</h2>
    <ol>
        <li><strong>Preprocessing</strong>: The dataset is cleaned, and important features are extracted.</li>
        <li><strong>Vectorization</strong>: The text-based features (genres, descriptions) are converted into numerical form using TF-IDF.</li>
        <li><strong>Similarity Calculation</strong>: Cosine similarity is used to find similar movies.</li>
        <li><strong>Recommendation Generation</strong>: When a user selects a movie, the system finds and displays similar movies.</li>
    </ol>

    <h2> Installation & Usage</h2>
    <h3>1️ Clone the Repository</h3>
    <pre><code>git clone https://github.com/ayushi-shahi/Movies-recommender-system.git
cd Movies-recommender-system</code></pre>

    <h3>2️ Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

   

    <h2> Deployment</h2>
    <p>This project can be deployed on <strong>Heroku</strong> using the following steps:</p>
    <pre><code>git add .
git commit -m "Deploying to Heroku"
git push heroku main</code></pre>
    <p>Make sure to add <code>Procfile</code> and <code>requirements.txt</code> for deployment.</p>

   
    <ul>
        <li>[ ] Add <strong>Collaborative Filtering</strong></li>
        <li>[ ] Improve UI/UX</li>
        <li>[ ] Deploy on <strong>Heroku</strong> with a better interface</li>
    </ul>

    <h2> Contributing</h2>
    <p>Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.</p>

    <h2> License</h2>
    <p>This project is <strong>MIT licensed</strong>.</p>

    <h2> Contact</h2>
    <p> <strong>LinkedIn</strong>: <a href="https://www.linkedin.com/in/ayushi-shahi-2907b0297" target="_blank">Ayushi Shahi</a></p>
    <p> <strong>Email</strong>: <a href="mailto:your-email@example.com">your-email@example.com</a></p>
</div>

</body>
</html>

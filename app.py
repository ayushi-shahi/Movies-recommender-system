import streamlit as st
import pickle
import pandas as pd
import requests
import time


def fetch_poster(movie_id):
    try:
        # API request to fetch movie data
        url = f'https://api.themoviesdb.org/3/movie/{movie_id}?api_key=6c6a222cdb28c55b0f4558f866f179d9&language=en-US'
        response = requests.get(url)

        # Debugging: Print response status and content
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        # If the response is valid, parse the JSON
        if response.status_code == 200:
            data = response.json()
            print(f"Parsed JSON: {data}")  # Debugging the parsed response

            # Check if poster_path exists
            poster_path = data.get('poster_path')
            if poster_path:
                poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
                print(f"Poster URL: {poster_url}")
                return poster_url
            else:
                print(f"No poster found for movie_id {movie_id}, returning default poster.")
                return "https://www.example.com/default_poster_image.jpg"  # Default image URL
        else:
            print(f"Error: Could not fetch poster for movie_id {movie_id} (Status Code: {response.status_code})")
            return "https://www.example.com/default_poster_image.jpg"  # Default image URL
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "https://www.example.com/default_poster_image.jpg"  # Default image for errors


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        time.sleep(1)  # Adding delay to avoid hitting API rate limit

    return recommended_movies, recommended_movies_posters


# Load the movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Display recommended movies with posters
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

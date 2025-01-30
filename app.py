import streamlit as st
import pickle
import pandas as pd
import requests
import time

API_KEY = "f467f77faf66425750f2ea7d1c2d775d"


def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            else:
                print(f"[Warning] No poster found for movie ID: {movie_id}")

        print(f"[Error] API request failed with status code {response.status_code}")
        return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.RequestException as e:
        print(f"[Exception] Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
            time.sleep(1)
        return recommended_movies, recommended_movies_posters
    except Exception as e:
        print(f"[Exception] Error in recommendation: {e}")
        return [], []


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie to get recommendations:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    if names:
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
    else:
        st.error("No recommendations found. Please check your movie selection.")

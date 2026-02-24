import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Movie Recommender 🎬",
    page_icon="🎥",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_resource

def load_data():
    movies_dict = pickle.load(open('movies.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

    movies = pd.DataFrame(movies_dict)
    vectors = vectorizer.transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)

    return movies, similarity

movies, similarity = load_data()


OMDB_API_KEY = "7cac9a10" 


@st.cache_data
def fetch_poster(movie_title):
    try:
        
        clean_title = movie_title.split("(")[0].strip()

        url = f"http://www.omdbapi.com/?t={clean_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=3)

        data = response.json()
        # print(data)
        if data.get("Response") == "True" and data.get("Poster") != "N/A":
            return data["Poster"]
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"

    except:
        return "https://via.placeholder.com/300x450?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for index, _ in movie_list:
        title = movies.iloc[index]['title']
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters

st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Find movies similar to your favorites</p>", unsafe_allow_html=True)

st.divider()

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].tolist()
)

if st.button("Recommend 🎬"):

    with st.spinner("Fetching recommendations..."):

        names, posters = recommend(selected_movie)

        st.subheader("Top Recommendations For You")

        cols = st.columns(5)

        for col, name, poster in zip(cols, names, posters):
            with col:
                st.image(poster)
                st.caption(name)

st.divider()
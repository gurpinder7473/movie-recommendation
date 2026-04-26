import streamlit as st
import pickle

# Load files
movie_matrix = pickle.load(open("movie_matrix.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie_name):
    movie_index = movie_matrix.columns.get_loc(movie_name)
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(movie_matrix.columns[i[0]])

    return recommendations

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Get movie recommendations based on collaborative filtering.")

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_matrix.columns
)

if st.button("Recommend Movies"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("✅", movie)

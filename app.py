import streamlit as st
import pickle
import requests
movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_df = movies_list
movies_list = movies_list['title'].values


def fetch_poster(movie_id):
    response =  requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b3786a390467799c11abd24aaa2ea7b4".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies_df[movies_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies:
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_df.iloc[i[0]].id))
       
    return recommended_movies,recommended_movies_posters
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which Movie Do You Like?',
    movies_list)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)
   
    with col1:
        st.caption(names[0])
        st.image(posters[0])

    with col2:
        st.caption(names[1])
        st.image(posters[1])

    with col3:
        st.caption(names[2])
        st.image(posters[2])
    with col4:
        st.caption(names[3])
        st.image(posters[3])
    with col5:
        st.caption(names[4])
        st.image(posters[4])


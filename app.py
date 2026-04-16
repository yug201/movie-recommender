import streamlit as st
import pickle
import pandas as pd
import requests
st.title("Movi Recommendation system")

movies = pd.read_csv("movies.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))


idx_titl={}
for i,x in enumerate(movies["title"]):
    idx_titl[x]=i
import time

def fetch_poster(movie_id):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1e77e2959feb1bd46f8e619971ce3765&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code!= 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data =response.json()

        poster_path=data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Poster"
        return "https://image.tmdb.org/t/p/w500/"+poster_path
    except requests.exceptions.RequestException as e:
        print("API Error:",e)
        return "https://via.placeholder.com/500x750?text=Error"

# movies["poster"] = movies["id"].apply(fetch_poster)

def recommend(movi,k=5):  #O(nlogn + k)==O(nlogn)  #  we can use heap in order to  descreas  time complexity  to  (O(n*log k))
    idx=idx_titl[movi]    #O(1)
    distances=similarity[idx]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])   #o(nlogn)
    res=[]
    for x in movies_list[1:min(k+1,len(idx_titl))]:  #O(k)
        res.append([movies["title"][x[0]],fetch_poster(movies["id"][x[0]])])
    return res




movies_list=list(movies["title"])
selected_movie =st.selectbox("movies",movies_list)
# if st.button("suggest"):
#     suggested=recommend(selected_movie,5)
#     for m in suggested:
#         st.write(m)



if st.button('Show Recommendation'):
    recommended_movie=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0][0])
        st.image(recommended_movie[0][1])
    with col2:
        st.text(recommended_movie[1][0])
        st.image(recommended_movie[1][1])

    with col3:
        st.text(recommended_movie[2][0])
        st.image(recommended_movie[2][1])
    with col4:
        st.text(recommended_movie[3][0])
        st.image(recommended_movie[3][1])
    with col5:
        st.text(recommended_movie[4][0])
        st.image(recommended_movie[4][1])

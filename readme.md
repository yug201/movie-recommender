#  Movie Recommendation System

A content-based movie recommendation system built using machine learning and deployed with Streamlit. It suggests similar movies based on genres, keywords, cast, crew, and overview.

---

##  Features

* Recommends top 5 similar movies
* Uses cosine similarity for comparison
* Displays movie posters using TMDB API
* Simple and interactive UI with Streamlit

---

##  Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* TMDB API

---

##  How It Works

1. Dataset is cleaned and merged (`tmdb_5000_movies` + `credits`)
2. Important features are extracted:

   * Genres
   * Keywords
   * Cast
   * Director
   * Overview
3. Text data is processed:

   * Tokenization
   * Stemming
   * Vectorization (CountVectorizer)
4. Cosine similarity is computed between movies
5. Top similar movies are recommended

---

##  Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  Files

* `movies.csv` → processed movie data
* `similarity.pkl` → similarity matrix
* `app.py` → Streamlit app

---

##  Example

Input: **Avatar**
Output: Similar movies like *Predator*, *Titan A.E.*, etc.

---

##  Note

* TMDB API key is required for fetching posters
* Replace the API key in `fetch_poster()`

---

If you want, I can also:

* Make it more professional (GitHub-level README with badges)
* Add screenshots section
* Or optimize your repo structure 👍

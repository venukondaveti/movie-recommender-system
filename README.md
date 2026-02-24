# 🎬 Movie Recommender System

A simple and interactive **Movie Recommender System** built using Machine Learning and deployed with Streamlit.

This application recommends movies similar to your favorite ones using **Content-Based Filtering**.

---

## 🚀 Live Demo

🔗 https://content-based-movie-recommender-systems.streamlit.app

---

## 📖 Overview

This project recommends movies based on their content features instead of user ratings.

It analyzes:
- Genres
- Keywords
- Cast
- Crew

All these features are combined into a single column called **tags**, converted into numerical vectors using `CountVectorizer`, and compared using **Cosine Similarity**.

---

## 🧠 How It Works

1. Movie metadata is cleaned and preprocessed in a Jupyter Notebook.
2. Important columns are merged into a single feature column.
3. Text data is converted into vectors using `CountVectorizer`.
4. Cosine similarity is calculated between movies.
5. When a user selects a movie, the system returns the top 5 most similar movies.
6. Posters are fetched dynamically using the OMDB API.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- OMDB API

---

## 📂 Project Structure
movie-recommender-system/
│
├── app.py
├── Movie_Recommnder_System.ipynb
├── movies.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venukondaveti/movie-recommender-system.git
cd movie-recommender-system

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

streamlit run app.py
```

### Author
Venu Kondaveti

Built as part of my Machine Learning learning journey.
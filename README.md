# 📚 Book Recommender System

A web-based book recommendation system built with **Python**, **Flask**, and **scikit-learn**. It combines a popularity-based approach and a collaborative filtering model to help users discover books they'll love.

---

## Project Overview

This system offers two ways to discover books:

- **Top 50 Popular Books** — Displays the most-rated and highest-rated books from the dataset on the home page
- **Personalized Recommendations** — Takes a book name as input and returns 5 similar books using collaborative filtering based on cosine similarity

---

## How It Works

### Popularity-Based Filtering
Books are ranked by number of ratings (minimum 250) and average rating, giving a reliable list of widely appreciated titles.

### Collaborative Filtering
- Users who have rated more than 200 books and books with at least 50 ratings are selected to reduce noise
- A pivot table is built mapping books to user ratings
- **Cosine similarity** is computed across book vectors to find titles with similar rating patterns
- The top 5 most similar books are returned for any given input

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| ML / Data | pandas, NumPy, scikit-learn |
| Frontend | HTML, Bootstrap 5 |
| Model Storage | Pickle |

---

## Dataset

The project uses the [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/), which contains:

| File | Records |
|------|---------|
| `Books.csv` | 271,360 books |
| `Users.csv` | 278,858 users |
| `Ratings.csv` | 1,149,780 ratings |

---

## Folder Structure

| Path | Description |
|------|-------------|
| `app.py` | Flask server and route definitions |
| `recommender.ipynb` | Data cleaning, EDA, and model training notebook |
| `popular.pkl` | Serialized popularity-based dataframe |
| `pt.pkl` | Serialized pivot table |
| `books.pkl` | Serialized books dataframe |
| `similarity_scores.pkl` | Serialized cosine similarity matrix |
| `templates/` | HTML templates (`index.html`, `recommend.html`) |

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### 2. Generate the Model Files

Run the Jupyter notebook `recommender.ipynb` end-to-end. This will generate the following pickle files in the root directory:

- `popular.pkl`
- `pt.pkl`
- `books.pkl`
- `similarity_scores.pkl`

### 3. Start the Flask App

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`

---

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home page — displays Top 50 popular books |
| `/recommend` | Input a book name to get 5 personalized recommendations |

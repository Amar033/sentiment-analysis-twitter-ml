# 🐦 Twitter Sentiment Analysis App

A full-stack AI-powered web app that analyzes the **sentiment of any tweet** using a trained machine learning model. Built with **React**, **FastAPI**, and **Scikit-learn**.

<div align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/Frontend-React-blue?logo=react" />
</div>

---

## 🚀 Demo

> 🎯 Enter a tweet and get instant sentiment prediction (Positive/Negative)

![demo](demo.gif) <!-- Replace with your actual demo.gif or screenshot -->

---

## 🧠 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| 🧠 ML Model   | Logistic Regression |
| 📊 Text Vectorization | TF-IDF             |
| ⚙ Backend    | FastAPI + Joblib    |
| 💻 Frontend  | React + Fetch API   |
| 🔗 Integration | CORS, REST API     |

---

## 📁 Folder Structure

sentiment-analysis-twiter-ml/
├── backend/
│ ├── main.py
│ ├── model/
│ │ ├── logistic_model.pkl
│ │ └── tfidf_vectorizer.pkl
│ └── requirements.txt
├── sentiment-frontend/
│ ├── App.js
│ ├── index.js
│ ├── App.css
│ └── package.json
├── notebook/
| └── eda.ipynb
└── README.md


---

## 💡 How it Works

1. **User** enters a tweet on the web interface.
2. The **React frontend** sends a POST request to FastAPI backend.
3. The **FastAPI server**:
   - Transforms the text using the `tfidf_vectorizer.pkl`
   - Predicts sentiment using `logistic_model.pkl`
4. The **prediction** is returned and displayed: `Positive` or `Negative`.

---

## 📦 Installation & Run Locally

### ⚙ Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 💻 Frontend (React)

```bash
cd sentiment-frontend
npm install
npm start
```

Make sure your backend (FastAPI) is running on http://localhost:8000
The frontend will run on http://localhost:3000


### Author
## Amardeep

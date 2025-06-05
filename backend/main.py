from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware

model=joblib.load("model/logistic_model.pkl")
vectorizer=joblib.load("model/tfidf_vectorizer.pkl")

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextInput(BaseModel):
    text: str

@app.post("/predict")
def sentiment(data :TextInput):
    vector = vectorizer.transform([data.text])
    prediction=model.predict(vector)[0]
    return {"sentiment":"Positive" if prediction==1 else "Negative"}

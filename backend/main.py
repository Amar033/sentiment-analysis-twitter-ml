from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                    "http://localhost:3001",
                    "https://sentiment-analysis-twitter-ml-wuzm.vercel.app",
                  "http://sentiment-analysis-twitter-ml-fxtj.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None
vectorizer = None

class TextInput(BaseModel):
    text: str

def load_models():
    global model, vectorizer
    
    try:
        if not os.path.exists("model/logistic_model.pkl"):
            raise FileNotFoundError("Model file not found: model/logistic_model.pkl")
        
        if not os.path.exists("model/tfidf_vectorizer.pkl"):
            raise FileNotFoundError("Vectorizer file not found: model/tfidf_vectorizer.pkl")
    
        model = joblib.load("model/logistic_model.pkl")
        vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
        
        print("Models loaded successfully!")
        return True
        
    except Exception as e:
        print(f"Error loading models: {e}")
        print("Current directory contents:", os.listdir("."))
        if os.path.exists("model"):
            print("Model directory contents:", os.listdir("model"))
        return False
load_models()

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API", "status": "running"}

@app.get("/health")
def health_check():
    if model is None or vectorizer is None:
        return {"status": "unhealthy", "reason": "Models not loaded"}
    return {"status": "healthy"}

@app.post("/predict")
def sentiment(data: TextInput):
    if model is None or vectorizer is None:
        if not load_models():
            raise HTTPException(status_code=503, detail="Models not available")
    
    try:
        vector = vectorizer.transform([data.text])
        prediction = model.predict(vector)[0]
        
        return {
            "text": data.text,
            "sentiment": "Positive" if prediction == 1 else "Negative",
            "prediction_value": int(prediction)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

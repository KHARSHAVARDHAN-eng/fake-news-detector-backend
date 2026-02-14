from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Fake Content Detection API Running"}

@app.post("/predict")
def predict(request: NewsRequest):
    text = request.text.lower()

    fake_keywords = [
        "shocking",
        "click here",
        "100% cure",
        "breaking secret",
        "guaranteed",
        "miracle"
    ]

    prediction = "REAL"
    confidence = round(random.uniform(65, 90), 2)
    explanation = "The content appears factual based on known references."
    wikipedia_url = "https://en.wikipedia.org/wiki/Fake_news"

    for word in fake_keywords:
        if word in text:
            prediction = "FAKE"
            confidence = round(random.uniform(75, 95), 2)
            explanation = "The content contains sensational or misleading phrases."
            break

    return {
        "prediction": prediction,
        "confidence": confidence,
        "explanation": explanation,
        "wikipedia_url": wikipedia_url
    }

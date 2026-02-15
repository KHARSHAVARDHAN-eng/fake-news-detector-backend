from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Fake Content Detection API Running"}

@app.post("/predict")
def predict(data: TextInput):
    text = data.text.lower()

    if "fake" in text or "click here" in text:
        return {"prediction": "Fake News"}
    else:
        return {"prediction": "Real News"}

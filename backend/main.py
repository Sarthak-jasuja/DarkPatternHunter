from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch.nn.functional as F

app = FastAPI()

# --- 1. SETUP CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. LOAD YOUR TRAINED AI ---
# We load this ONCE when the server starts so it's fast
print("Loading AI Model...")
MODEL_PATH = "./dark_pattern_model" 
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval() # Tell model we are predicting, not training

# Define the labels (These must match what you trained on)
# If you used the Venkatesh4342 dataset, the labels map roughly to:
LABELS = {
    0: "Dark Pattern",
    1: "Safe"
}

class PageText(BaseModel):
    texts: List[str]

@app.post("/analyze")
async def analyze_page(payload: PageText):
    results = []
    
    for text in payload.texts:
        if len(text.split()) < 4: 
            continue
            
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
        
        with torch.no_grad():
            outputs = model(**inputs)
            
        probs = F.softmax(outputs.logits, dim=1)
        confidence, predicted_class = torch.max(probs, dim=1)
        predicted_index = predicted_class.item()
        score = confidence.item()
        if predicted_index == 0 and score > 0.85:
            results.append({
                "text": text,
                "label": "Potential Dark Pattern", # Since model is binary, we use a generic label
                "score": round(score, 2)
            })

    return {"patterns": results}
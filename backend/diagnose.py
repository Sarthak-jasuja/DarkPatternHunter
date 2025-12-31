import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch.nn.functional as F

# 1. Load your local model
MODEL_PATH = "./dark_pattern_model"
try:
    tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
    model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit()

# 2. Define 3 specific test sentences
test_sentences = [
    ("HURRY", "Hurry! This offer expires in 5 minutes!"),            # Should be Urgency
    ("SAFE",  "This is a standard water bottle made of glass."),     # Should be Not Dark
    ("RARE",  "Only 1 item left in stock at this price."),           # Should be Scarcity
]

print(f"\n🔍 DIAGNOSTIC REPORT for {MODEL_PATH}")
print("-" * 60)
print(f"{'TYPE':<10} | {'PREDICTED ID':<15} | {'CONFIDENCE':<10} | {'RAW SCORES (IDs 0,1,2...)'}")
print("-" * 60)

for name, text in test_sentences:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get probabilities
    probs = F.softmax(outputs.logits, dim=1)[0]
    confidence, predicted_id = torch.max(probs, dim=0)
    
    # Format raw scores for display
    raw_scores = ", ".join([f"{p:.2f}" for p in probs])
    
    print(f"{name:<10} | ID {predicted_id.item():<12} | {confidence.item():.2f}       | [{raw_scores}]")

print("-" * 60)
print("INTERPRETATION:")
print("1. Look at the 'SAFE' row. The ID it picked is likely 'Not Dark Pattern'.")
print("2. Look at the 'HURRY' row. The ID it picked is likely 'Urgency'.")
print("3. Update your main.py LABELS dictionary to match these IDs.")
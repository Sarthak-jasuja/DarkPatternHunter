🕵️‍♀️ #The Dark Pattern Hunter
AI-Powered Protection Against Manipulative Web Design

The Dark Pattern Hunter is a browser extension that uses a fine-tuned Large Language Model (LLM) to detect and highlight "Dark Patterns" in real-time. It analyzes the semantic meaning of web content to flag manipulative UI elements like Urgency, Scarcity, Social Proof, and Hidden Costs.

🎥 Demo
![Dark Pattern Hunter Demo]([Insert Link to GIF or Screenshot of your index.html here]) Above: The extension detecting "Fake Urgency" and "Hidden Costs" on a demo e-commerce site.

🚀 Features
Real-Time Analysis: Scrapes visible text from the DOM and processes it instantly.

AI-Powered: Uses a fine-tuned DistilBERT (or Gemma 2B) model, not just keyword matching.

Privacy First: Analysis happens locally (or via a private API), ensuring user data isn't harvested.

Visual Highlights: Automatically draws a red border around manipulative text.

🛠️ Tech Stack
Frontend: Chrome Extension (JavaScript, Manifest V3)

Backend: Python, FastAPI, Uvicorn

AI Engine: PyTorch, Hugging Face Transformers

Model: DistilBERT (Fine-tuned on the Princeton Dark Patterns Dataset)

📦 Installation
1. Clone the Repository

Bash
git clone https://github.com//DarkPatternHunter.git
cd DarkPatternHunter
2. Setup Backend (The Brain)

Bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
The server will start at http://127.0.0.1:8000

3. Load Extension (The Eye)

Open Chrome and navigate to chrome://extensions/

Toggle Developer Mode (top right).

Click Load Unpacked.

Select the extension folder from this repository.

🧪 How to Test
I have included a "Trap Website" to test the model's detection capabilities.

Navigate to the project folder.

Run a local server:

Bash
python3 -m http.server 5500
Open http://localhost:5500/index.html in Chrome.

Watch the AI flag the specific "Urgency" and "Scarcity" zones while ignoring the legitimate text.

🧠 Model Training
The model was fine-tuned using the Dark Patterns at Scale dataset.

Base Model: distilbert-base-uncased

Training Loss: 0.12

Accuracy: ~94% on validation set.

Note: For the advanced version, check the experimental branch where I implemented QLoRA fine-tuning on Google's Gemma-2B.

📜 License
MIT License

Tips for your Video Voiceover while showing index.html

When your video reaches the part where index.html is on screen:

Point out the "Safe" zone first:

Say: "Notice how the Standard Plan description remains clean. The AI understands that factual product descriptions are safe."

Then point to the "Red" zone:

Say: "But look at the Premium Plan. It flagged 'Only 2 spots left' and the countdown timer. It recognizes this as Artificial Scarcity."

Mention the 'Fine Print':

Say: "It even caught the hidden fees buried in the footer text, which keyword-based blockers usually miss."

This contrast (Safe vs. Unsafe) is what proves your AI is actually "thinking" and not just highlighting every number it sees.
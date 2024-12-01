Predictive Analytics for Social Media Virality

This project focuses on predicting the virality of social media content, identifying key influencers, and assessing misinformation spread using advanced machine learning and deep learning models. The system is built using Python (FastAPI for backend) and JavaScript (React for frontend).

---

Features
1. **Virality Prediction**: Analyze content engagement metrics to predict virality.
2. **Influencer Identification**: Evaluate user data to identify influential users.
3. **Misinformation Assessment**: Detect and assess the spread of potential misinformation.

---

Installation and Setup

### Prerequisites
- Python 3.8+
- Node.js
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/MoSahil147/social-media-analytics.git
cd social-media-analytics
```

###Step 2: Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt 
```
###Step 3: Frontend Setup
```bash
cd ../frontend
npm install
```
###Step 4: Train Model
```bash
python backend/train/train_virality.py
python backend/train/train_influencer.py
python backend/train/train_diffusion.py
```
###Step 5: Start the Backend
```bash
cd backend
uvicorn app:app --reload
```
The backend will run at http://127.0.0.1:8000

###Step 6: Start the Frontend
```bash
cd ../frontend
npm start
```
The frontend will run at http://localhost:3000

API Endpoints

	•	/virality: Predicts the virality score of content.
	•	/influencer: Calculates influencer scores.
	•	/diffusion: Evaluates misinformation spread.

Results

	1.	Virality Prediction:
	•	Accuracy: 92.34%
	•	F1 Score: 0.91
 
	2.	Influencer Identification:
	•	Accuracy: 89.12%
	•	Precision: 0.89
 
	3.	Misinformation Assessment:
	•	Accuracy: 87.45%
	•	Recall: 0.86

Feel free to fork the repository and submit pull requests. 😊 
 

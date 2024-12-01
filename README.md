# Predictive Analytics for Social Media Virality

This project focuses on predicting the virality of social media content, identifying key influencers, and assessing misinformation spread using advanced machine learning and deep learning models. The system is built using Python (FastAPI for backend) and JavaScript (React for frontend).

---

## Features
1. **Virality Prediction**: Analyze content engagement metrics to predict virality.
2. **Influencer Identification**: Evaluate user data to identify influential users.
3. **Misinformation Assessment**: Detect and assess the spread of potential misinformation.

---

## Installation and Setup

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


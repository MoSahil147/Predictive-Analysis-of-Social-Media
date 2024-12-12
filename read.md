# Social Media Analytics Platform

A comprehensive web-based platform for social media analytics, built using a machine learning-powered backend and a React frontend. This platform predicts virality, identifies influencers, and detects misinformation diffusion.

Project Installation and Working 

### Step 1: Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt 
```

### Step 2: Frontend Setup
```bash
cd ../frontend
npm install
```

### Step 3: Train Model
```bash
python backend/train/train_virality.py
python backend/train/train_influencer.py
python backend/train/train_diffusion.py
```
### Step 4: Train Model
```bash
python backend/evaluation/calculate_virality_metrics.py
python backend/evaluation/calculate_influencer_metrics.py
python backend/evaluation/calculate_diffusion_metrics.py
```

### Step 5: Start the Backend
```bash
cd backend
uvicorn app:app --reload
```

The backend will run at http://127.0.0.1:8000

### Step 6: Start the Frontend
```bash
cd ../frontend
npm start
```

The frontend will run at http://localhost:3000




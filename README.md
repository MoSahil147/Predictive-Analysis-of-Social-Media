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

The Folder Structure

social_media_analytics/
├── backend/                                # Backend folder for processing and predictions
│   ├── app.py                              # Main FastAPI app for API endpoints
│   ├── models/                             # Directory for ML model definitions
│   │   ├── virality_model.py               # Virality Prediction Model
│   │   ├── influencer_model.py             # Influencer Identification Model
│   │   ├── diffusion_model.py              # Diffusion Prediction Model (Misinformation Assessment)
│   │   ├── __init__.py                     # Package initializer for models
│   ├── preprocess/                         # Preprocessing functions for ML models
│   │   ├── virality_preprocess.py          # Preprocessing for Virality Prediction
│   │   ├── influencer_preprocess.py        # Preprocessing for Influencer Identification
│   │   ├── diffusion_preprocess.py         # Preprocessing for Diffusion Prediction
│   │   ├── __init__.py                     # Package initializer for preprocess
│   ├── train/                              # Training scripts for models
│   │   ├── train_virality.py               # Training script for Virality Prediction Model
│   │   ├── train_influencer.py             # Training script for Influencer Identification Model
│   │   ├── train_diffusion.py              # Training script for Diffusion Prediction Model
│   ├── scalers/                            # Scalers used during preprocessing
│   │   ├── virality_scaler.pkl             # Scaler for Virality Prediction
│   │   ├── influencer_scaler.pkl           # Scaler for Influencer Identification
│   │   ├── diffusion_scaler.pkl            # Scaler for Diffusion Prediction
│   ├── data/                               # Datasets for training and testing
│   │   ├── virality_data.csv               # Dataset for Virality Prediction
│   │   ├── influencer_data.csv             # Dataset for Influencer Identification
│   │   ├── diffusion_data.csv              # Dataset for Diffusion Prediction
│   ├── convert_to_onnx/                    # Scripts for ONNX conversion
│   │   ├── convert_virality_to_onnx.py     # Convert Virality Model to ONNX format
│   │   ├── convert_influencer_to_onnx.py   # Convert Influencer Model to ONNX format
│   │   ├── convert_diffusion_to_onnx.py    # Convert Diffusion Model to ONNX format
│   ├── utils/                              # Utility scripts
│   │   ├── batch_processing.py             # Functions for batch processing data
│   │   ├── __init__.py                     # Package initializer for utils
│   ├── requirements.txt                    # Backend dependencies
│
├── frontend/                               # Frontend folder for user interface
│   ├── index.html                          # Main landing page (Intro page)
│   ├── style.css                           # Global CSS for shared styles
│   ├── intro.js                            # JavaScript for Intro page interactions
│   ├── images/                             # Image assets
│   │   ├── intro.jpg                       # Background for main intro section
│   │   ├── pic1.jpg                        # Virality Prediction image
│   │   ├── pic2.jpg                        # Influencer Prediction image
│   │   ├── pic3.jpg                        # Diffusion Prediction image
│   │   ├── Back.jpg                        # Shared background image
│   ├── ViralityPredictionTool/             # Virality Prediction Module
│   │   ├── virality_prediction.html        # Form to input virality data
│   │   ├── toolpred.css                    # CSS for Virality Prediction page
│   │   ├── virality.js                     # JavaScript for handling form submission
│   │   └── ViralityScore/                  # Display results of Virality Prediction
│   │       ├── virality_score.html         # Page to display virality score
│   │       ├── virality_score.css          # CSS for virality score page
│   │       └── virality_score.js           # JavaScript for score animations
│   ├── InfluencerIdentificationModel/      # Influencer Identification Module
│   │   ├── influ.html                      # Form to input influencer data
│   │   ├── fluin.css                       # CSS for Influencer Identification page
│   │   ├── influencer.js                   # JavaScript for handling form submission
│   │   └── InfluencerScore/                # Display results of Influencer Identification
│   │       ├── influencer_score.html       # Page to display influencer score
│   │       ├── influencer_score.css        # CSS for influencer score page
│   │       └── influencer_score.js         # JavaScript for score animations
│   ├── DiffusionPredictionModel/           # Diffusion Prediction (Misinformation) Module
│   │   ├── diffu.html                      # Form to input diffusion data
│   │   ├── difupred.css                    # CSS for Diffusion Prediction page
│   │   ├── diffusion.js                    # JavaScript for handling form submission
│   │   └── MisinformationScore/            # Display results of Misinformation Assessment
│   │       ├── misinformation_status.html  # Page to display misinformation score
│   │       ├── misinformation_status.css   # CSS for misinformation score page
│   │       └── misinformation_status.js    # JavaScript for score animations
│   ├── package.json                        # Frontend dependencies
│
└── README.md                               # Project documentation

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
 

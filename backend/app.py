# app.py in the backend folder

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust according to your frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model for Virality
class ViralityRequest(BaseModel):
    likes: float
    shares: float
    comments: float
    weakTies: float

# Define request model for Influencer
class InfluencerRequest(BaseModel):
    followers: float
    posts: float
    likes: float
    comments: float
    engagementRate: float

# Define request model for Diffusion (Misinformation)
class DiffusionRequest(BaseModel):
    likes: float
    shares: float
    comments: float
    engagementRate: float

# Define /virality endpoint
@app.post("/virality")
async def calculate_virality(data: ViralityRequest):
    # Example calculation logic for virality score
    score = (data.likes + data.shares + data.comments + data.weakTies) / 4
    virality_score = min(max(score, 0), 100)  # Clamp score between 0 and 100
    return {"viralityScore": round(virality_score, 2)}

# Define /influencer endpoint
@app.post("/influencer")
async def calculate_influencer(data: InfluencerRequest):
    # Example calculation logic for influencer score
    score = (data.followers + data.posts + data.likes + data.comments + data.engagementRate) / 5
    influencer_score = min(max(score, 0), 100)  # Clamp score between 0 and 100
    return {"influencerScore": round(influencer_score, 2)}

# Define /diffusion endpoint
@app.post("/diffusion")
async def calculate_diffusion(data: DiffusionRequest):
    # Example calculation logic for misinformation score
    score = (data.likes + data.shares + data.comments + data.engagementRate) / 4
    misinformation_score = min(max(score, 0), 100)  # Clamp score between 0 and 100
    return {"misinformationScore": round(misinformation_score, 2)}
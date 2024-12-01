# Import FastAPI to create the app
from fastapi import FastAPI 

# Import BaseModel from Pydantic to define the structure of the data received in requests
from pydantic import BaseModel 

# Import CORS middleware to handle cross-origin resource sharing
from fastapi.middleware.cors import CORSMiddleware 

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware to allow the app to communicate with a frontend or other services on different domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (any computer or domain)
    allow_credentials=True,  # Allow credentials like cookies in the request
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers in the request
)

# Define the data model for the /virality endpoint using Pydantic's BaseModel
class ViralityRequest(BaseModel):
    likes: float  # Number of likes (expects a floating-point number)
    shares: float  # Number of shares
    comments: float  # Number of comments
    weakTies: float  # Measure of weak ties (a parameter related to virality)

# Define the data model for the /influencer endpoint
class InfluencerRequest(BaseModel):
    followers: float  # Number of followers
    posts: float  # Number of posts
    likes: float  # Number of likes
    comments: float  # Number of comments
    engagementRate: float  # Engagement rate as a percentage

# Define the data model for the /diffusion endpoint
class DiffusionRequest(BaseModel):
    likes: float  # Number of likes
    shares: float  # Number of shares
    comments: float  # Number of comments
    engagementRate: float  # Engagement rate as a percentage

# Define the /virality endpoint to calculate the virality score
@app.post("/virality")
async def calculate_virality(data: ViralityRequest):
    # Calculate the virality score using a simple average formula
    score = (data.likes + data.shares + data.comments + data.weakTies) / 4
    virality_score = min(max(score, 0), 100)  # Clamp the score between 0 and 100
    return {"viralityScore": round(virality_score, 2)}  # Return the score rounded to two decimal places

# Define the /influencer endpoint to calculate the influencer score
@app.post("/influencer")
async def calculate_influencer(data: InfluencerRequest):
    # Calculate the influencer score using a simple average formula
    score = (data.followers + data.posts + data.likes + data.comments + data.engagementRate) / 5
    influencer_score = min(max(score, 0), 100)  # Clamp the score between 0 and 100
    return {"influencerScore": round(influencer_score, 2)}  # Return the score rounded to two decimal places

# Define the /diffusion endpoint to calculate the misinformation score
@app.post("/diffusion")
async def calculate_diffusion(data: DiffusionRequest):
    # Calculate the misinformation score using a simple average formula
    score = (data.likes + data.shares + data.comments + data.engagementRate) / 4
    misinformation_score = min(max(score, 0), 100)  # Clamp the score between 0 and 100
    return {"misinformationScore": round(misinformation_score, 2)}  # Return the score rounded to two decimal places

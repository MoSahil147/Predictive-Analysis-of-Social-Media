## This file defines the main FastAPI application.
## It creates the API endpoints for virality, influencer, and diffusion prediction.
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

## This section sets up Cross-Origin Resource Sharing (CORS) middleware.
## CORS is a security feature that prevents web pages from making requests to a different domain than the one that served the page.
## By adding this middleware, we can allow our frontend (running on a different domain) to communicate with our backend API.
## allow_origins=["*"] allows all origins, which is convenient for development, but for production, it's better to restrict this to the specific domain of your frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## These classes define the structure of the data that our API expects in the request body for each endpoint.
## Pydantic models are used for data validation and serialization.
## This ensures that we receive the data in the correct format, and it also helps with generating API documentation.
class ViralityRequest(BaseModel):
    likes: float
    shares: float
    comments: float
    weakTies: float

class InfluencerRequest(BaseModel):
    followers: float
    posts: float
    likes: float
    comments: float
    engagementRate: float

class DiffusionRequest(BaseModel):
    likes: float
    shares: float
    comments: float
    engagementRate: float

## These are the API endpoints. Each function handles a POST request to a specific path.
## The functions take a request body that matches the corresponding Pydantic model.
## The logic inside each function is a placeholder and should be replaced with the actual model prediction logic.

@app.post("/virality")
async def calc_virality(d: ViralityRequest):
    ## This endpoint calculates a virality score based on the input data.
    ## The current implementation is a simple average of the input features.
    ## In a real-world scenario, this is where you would load your trained virality model and use it to predict the score.
    score = (d.likes + d.shares + d.comments + d.weakTies) / 4
    return {"viralityScore": round(min(max(score, 0), 100), 2)}

@app.post("/influencer")
async def calc_influencer(d: InfluencerRequest):
    ## This endpoint calculates an influencer score based on the input data.
    ## The current implementation is a simple average of the input features.
    ## In a real-world scenario, this is where you would load your trained influencer model and use it to predict the score.
    score = (
        d.followers + d.posts + d.likes + d.comments + d.engagementRate
    ) / 5
    return {"influencerScore": round(min(max(score, 0), 100), 2)}

@app.post("/diffusion")
async def calc_diffusion(d: DiffusionRequest):
    ## This endpoint calculates a diffusion (misinformation) score based on the input data.
    ## The current implementation is a simple average of the input features.
    ## In a real-world scenario, this is where you would load your trained diffusion model and use it to predict the score.
    score = (d.likes + d.shares + d.comments + d.engagementRate) / 4
    return {"misinformationScore": round(min(max(score, 0), 100), 2)}
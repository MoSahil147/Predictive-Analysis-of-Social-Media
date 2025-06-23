from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ---- CORS: allow GitHub-Pages frontend -------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mosahil147.github.io",
        "https://mosahil147.github.io/Predictive-Analysis-of-Social-Media",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Pydantic request models ------------------------------------------------
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

# ---- End-points -------------------------------------------------------------
@app.post("/virality")
async def calc_virality(d: ViralityRequest):
    score = (d.likes + d.shares + d.comments + d.weakTies) / 4
    return {"viralityScore": round(min(max(score, 0), 100), 2)}

@app.post("/influencer")
async def calc_influencer(d: InfluencerRequest):
    score = (
        d.followers + d.posts + d.likes + d.comments + d.engagementRate
    ) / 5
    return {"influencerScore": round(min(max(score, 0), 100), 2)}

@app.post("/diffusion")
async def calc_diffusion(d: DiffusionRequest):
    score = (d.likes + d.shares + d.comments + d.engagementRate) / 4
    return {"misinformationScore": round(min(max(score, 0), 100), 2)}
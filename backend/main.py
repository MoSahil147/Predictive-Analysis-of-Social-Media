from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ViralityRequest(BaseModel):
    likes: float
    shares: float
    comments: float
    weakTies: float

@app.post("/virality")
async def calculate_virality(data: ViralityRequest):
    # Example logic for calculating virality score
    # Replace this with your actual calculation logic
    score = (data.likes + data.shares + data.comments + data.weakTies) / 4

    # Convert to percentage format (0-100) if necessary
    virality_score = min(max(score, 0), 100)  # Clamp score between 0 and 100

    return {"viralityScore": round(virality_score, 2)}

# To verify the server is running
@app.get("/")
async def root():
    return {"message": "Welcome to the Social Media Virality Prediction API"}
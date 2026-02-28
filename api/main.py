from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.graph import content_machine

import os

# Load environment variables from the .env file at the root of your project
load_dotenv()

# Initialize the FastAPI application
app = FastAPI(
    title="Tiny Content Machine API",
    description="A multi-agent orchestration API for repurposing long-form content.",
    version="1.0.0"
)

# Define the incoming request structure
class ContentRequest(BaseModel):
    source_text: str

# Define the outgoing response structure
class ContentResponse(BaseModel):
    brand_voice: str
    reel_script: str
    carousel: str
    twitter_thread: str
    static_caption: str

@app.post("/generate", response_model=ContentResponse)
async def generate_content(request: ContentRequest):
    # 1. Security Check: Ensure the API key exists
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500, 
            detail="OPENAI_API_KEY is not set. Please add it to your .env file."
        )
    
    try:
        # 2. Trigger the LangGraph Multi-Agent System
        # We pass the initial state (just the source_text) into the compiled graph
        result = content_machine.invoke({"source_text": request.source_text})
        
        # 3. Return the populated state back to the frontend
        return ContentResponse(
            brand_voice=result.get("brand_voice", ""),
            reel_script=result.get("reel_script", ""),
            carousel=result.get("carousel", ""),
            twitter_thread=result.get("twitter_thread", ""),
            static_caption=result.get("static_caption", "")
        )
        
    except Exception as e:
        # Catch any errors from OpenAI or LangGraph and return a clean HTTP 500 error
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")
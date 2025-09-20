"""
Oracle Backend API - Connects web interface to Gemini AI
Handles user queries and returns AI-generated responses
"""

import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import google.generativeai as genai
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(title="Oracle Backend API", version="1.0.0")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    question: str
    context: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    status: str

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None
    print("Warning: GEMINI_API_KEY not found. Using fallback responses.")

@app.get("/")
async def root():
    return {"message": "Oracle Backend API is running", "status": "active"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "gemini_configured": GEMINI_API_KEY is not None,
        "model_available": model is not None
    }

@app.post("/oracle/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process user query through Gemini AI and return response
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        if model is not None:
            # Use Gemini API
            prompt = f"""You are an Oracle providing thoughtful, creative guidance. 
            Respond to this question with wisdom and insight:
            
            Question: {request.question}
            
            Provide a meaningful, helpful response that encourages creativity and growth."""
            
            response = model.generate_content(prompt)
            answer = response.text
        else:
            # Fallback response when Gemini API not available
            answer = f"I hear your question: '{request.question}'. While I cannot access external AI services at the moment, I encourage you to explore this question deeply. Consider what creative possibilities it opens, what new perspectives it might reveal, and how it connects to your broader journey of growth and discovery."
        
        return QueryResponse(
            answer=answer,
            status="success"
        )
    
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.post("/oracle/speak")
async def get_speech_response(request: QueryRequest):
    """
    Get response formatted for speech synthesis
    """
    try:
        # Process the query first
        query_response = await process_query(request)
        
        # Format response for better speech synthesis
        speech_text = query_response.answer
        
        # Remove markdown formatting that doesn't work well with TTS
        speech_text = speech_text.replace("**", "").replace("*", "")
        speech_text = speech_text.replace("#", "").replace("`", "")
        
        return {
            "text": speech_text,
            "status": "success"
        }
    
    except Exception as e:
        print(f"Error generating speech response: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating speech response: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    print("Starting Oracle Backend API...")
    print("Frontend should connect to: http://127.0.0.1:8001")
    uvicorn.run(app, host="127.0.0.1", port=8001)
"""
Oracle Creative Inspiration Tool - Complete Integration
Autonomous AI agent for creative guidance and inspiration
"""

import os
import json
import asyncio
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import google.generativeai as genai
from typing import Optional
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Oracle Creative Inspiration API", 
    version="2.0.0",
    description="AI-powered creative inspiration and guidance system"
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    question: str
    context: Optional[str] = None
    creativity_level: Optional[str] = "balanced"  # minimal, balanced, expansive

class QueryResponse(BaseModel):
    answer: str
    status: str
    inspiration_type: str
    creativity_score: int

class HealthResponse(BaseModel):
    status: str
    ai_enabled: bool
    model_ready: bool
    timestamp: str

# Configure Gemini AI with enhanced creative prompts
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = None

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        logger.info("Gemini AI model initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Gemini AI: {e}")
        model = None
else:
    logger.warning("GEMINI_API_KEY not configured - using fallback responses")

# Creative inspiration templates
CREATIVE_PROMPTS = {
    "minimal": """You are a focused Oracle of Creative Insight. Provide a concise, actionable response to: {question}
    
    Focus on one clear creative direction or insight. Be specific and practical.""",
    
    "balanced": """You are an Oracle of Creative Potential, bridging practical wisdom with imaginative possibility. 
    
    Question: {question}
    
    Provide thoughtful guidance that balances creativity with actionable insights. Include both immediate steps and broader creative possibilities.""",
    
    "expansive": """You are the Oracle of Infinite Creative Potential, channeling boundless inspiration and visionary insight.
    
    Question: {question}
    
    Explore multiple creative dimensions, unexpected connections, and transformative possibilities. Include actionable steps, creative challenges, and inspirational directions. Think beyond conventional boundaries."""
}

FALLBACK_RESPONSES = {
    "creative": "Creative potential flows like water - it finds new paths when met with obstacles. Your question reveals an opening for innovation. Consider: What if the constraint you see is actually the gateway to breakthrough?",
    "inspiration": "True inspiration often emerges at the intersection of preparation and spontaneity. Your inquiry suggests you're prepared - now create space for the unexpected to arrive.",
    "guidance": "The path forward becomes clear when we stop forcing and start flowing. Your question indicates readiness for the next creative leap."
}

@app.get("/", response_class=FileResponse)
async def serve_frontend():
    """Serve the main Oracle interface"""
    return FileResponse("oracle_voice_interface.html")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Enhanced health check with system status"""
    from datetime import datetime
    return HealthResponse(
        status="healthy",
        ai_enabled=GEMINI_API_KEY is not None,
        model_ready=model is not None,
        timestamp=datetime.now().isoformat()
    )

@app.post("/oracle/query", response_model=QueryResponse)
async def process_creative_query(request: QueryRequest):
    """Process creative queries with enhanced AI guidance"""
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        creativity_level = request.creativity_level or "balanced"
        
        if model is not None:
            # Use Gemini AI with creative enhancement
            prompt_template = CREATIVE_PROMPTS.get(creativity_level, CREATIVE_PROMPTS["balanced"])
            prompt = prompt_template.format(question=request.question)
            
            if request.context:
                prompt += f"\n\nAdditional context: {request.context}"
            
            response = model.generate_content(prompt)
            answer = response.text
            
            # Analyze creativity level of response
            creativity_score = min(100, len(answer.split()) + creativity_level == "expansive" * 20)
            inspiration_type = "ai_generated"
            
        else:
            # Enhanced fallback responses
            import random
            fallback_key = random.choice(list(FALLBACK_RESPONSES.keys()))
            answer = FALLBACK_RESPONSES[fallback_key]
            creativity_score = 75
            inspiration_type = "curated_wisdom"
        
        return QueryResponse(
            answer=answer,
            status="success",
            inspiration_type=inspiration_type,
            creativity_score=creativity_score
        )
    
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.post("/oracle/speak")
async def get_speech_response(request: QueryRequest):
    """Get response optimized for speech synthesis"""
    try:
        query_response = await process_creative_query(request)
        
        # Optimize for speech
        speech_text = query_response.answer
        speech_text = speech_text.replace("**", "").replace("*", "")
        speech_text = speech_text.replace("#", "").replace("`", "")
        speech_text = speech_text.replace("\n\n", ". ").replace("\n", " ")
        
        return {
            "text": speech_text,
            "status": "success",
            "inspiration_type": query_response.inspiration_type,
            "creativity_score": query_response.creativity_score
        }
    
    except Exception as e:
        logger.error(f"Error generating speech response: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Speech generation error: {str(e)}")

@app.get("/oracle/inspire")
async def get_random_inspiration():
    """Generate random creative inspiration"""
    inspirations = [
        "What if the solution you seek already exists in an unexpected form?",
        "Creative breakthrough often requires embracing what seems impossible.",
        "The intersection of your unique experiences holds untapped potential.",
        "What would you create if failure was impossible?",
        "The most profound innovations often start with simple questions.",
        "Your creative constraints are actually design parameters in disguise."
    ]
    
    import random
    return {
        "inspiration": random.choice(inspirations),
        "status": "success",
        "type": "spontaneous"
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Oracle Creative Inspiration System...")
    logger.info("Serving interface at: http://127.0.0.1:8001")
    logger.info("API documentation at: http://127.0.0.1:8001/docs")
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="info")
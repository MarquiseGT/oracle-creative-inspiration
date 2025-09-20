"""
Oracle Enhanced - Cloud-Ready Version
Production-optimized FastAPI backend for public deployment
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

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI with production settings
app = FastAPI(
    title="Oracle Creative Inspiration API", 
    version="2.1.0",
    description="Cloud-deployed AI-powered creative inspiration system",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Enhanced CORS for public deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure specific domains in production
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    question: str
    context: Optional[str] = None
    creativity_level: Optional[str] = "balanced"

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
    version: str

# Configure Gemini AI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = None

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        logger.info("✅ Gemini AI model initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize Gemini AI: {e}")
        model = None
else:
    logger.warning("⚠️ GEMINI_API_KEY not configured - using fallback responses")

# Enhanced creative prompts for public use
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

FALLBACK_RESPONSES = [
    "Creative potential flows like water - it finds new paths when met with obstacles. Your question reveals an opening for innovation. Consider: What if the constraint you see is actually the gateway to breakthrough?",
    "True inspiration often emerges at the intersection of preparation and spontaneity. Your inquiry suggests you're prepared - now create space for the unexpected to arrive.",
    "The path forward becomes clear when we stop forcing and start flowing. Your question indicates readiness for the next creative leap.",
    "Innovation thrives in the space between what is and what could be. Your question opens that space - what will you create there?",
    "Every creative challenge contains its own solution. Your question shows you're already seeing beyond the obvious - trust that vision.",
    "The most profound breakthroughs come from asking better questions, not finding perfect answers. Your inquiry is already a creative act."
]

@app.get("/")
async def serve_frontend():
    """Serve the main Oracle interface"""
    try:
        return FileResponse("oracle_voice_interface.html")
    except FileNotFoundError:
        return JSONResponse({
            "message": "Oracle Creative Inspiration API",
            "status": "active",
            "frontend": "Interface available at /oracle",
            "api_docs": "/api/docs"
        })

@app.get("/oracle")
async def serve_oracle_interface():
    """Serve Oracle interface at dedicated endpoint"""
    try:
        return FileResponse("oracle_voice_interface.html")
    except FileNotFoundError:
        return JSONResponse({
            "error": "Oracle interface not found",
            "api_available": True,
            "endpoints": ["/health", "/oracle/query", "/oracle/speak", "/oracle/inspire"]
        })

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Production health check with detailed status"""
    from datetime import datetime
    return HealthResponse(
        status="healthy",
        ai_enabled=GEMINI_API_KEY is not None,
        model_ready=model is not None,
        timestamp=datetime.now().isoformat(),
        version="2.1.0"
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
            
            # Calculate creativity metrics
            creativity_score = min(100, len(answer.split()) + (20 if creativity_level == "expansive" else 10))
            inspiration_type = "ai_generated"
            
        else:
            # Enhanced fallback responses
            import random
            answer = random.choice(FALLBACK_RESPONSES)
            creativity_score = 85
            inspiration_type = "curated_wisdom"
        
        logger.info(f"Query processed: {request.question[:50]}...")
        
        return QueryResponse(
            answer=answer,
            status="success",
            inspiration_type=inspiration_type,
            creativity_score=creativity_score
        )
    
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Unable to process creative query")

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
        raise HTTPException(status_code=500, detail="Unable to generate speech response")

@app.get("/oracle/inspire")
async def get_random_inspiration():
    """Generate random creative inspiration"""
    inspirations = [
        "What if the solution you seek already exists in an unexpected form?",
        "Creative breakthrough often requires embracing what seems impossible.",
        "The intersection of your unique experiences holds untapped potential.",
        "What would you create if failure was impossible?",
        "The most profound innovations often start with simple questions.",
        "Your creative constraints are actually design parameters in disguise.",
        "Innovation happens when preparation meets spontaneous insight.",
        "The edge of your comfort zone is where creativity begins.",
        "Every limitation is an invitation to find a new path.",
        "Your perspective is the unique ingredient no one else can provide."
    ]
    
    import random
    return {
        "inspiration": random.choice(inspirations),
        "status": "success",
        "type": "spontaneous",
        "creativity_score": random.randint(80, 95)
    }

@app.get("/api/status")
async def api_status():
    """API status for monitoring"""
    return {
        "api": "Oracle Creative Inspiration",
        "version": "2.1.0",
        "status": "operational",
        "ai_model": "gemini-pro" if model else "fallback",
        "endpoints": {
            "query": "/oracle/query",
            "speech": "/oracle/speak", 
            "inspiration": "/oracle/inspire",
            "health": "/health"
        }
    }

if __name__ == "__main__":
    import uvicorn
    
    # Production server configuration
    port = int(os.getenv("PORT", 8001))
    host = os.getenv("HOST", "0.0.0.0")
    
    logger.info("🚀 Starting Oracle Creative Inspiration System...")
    logger.info(f"🌐 Server: http://{host}:{port}")
    logger.info(f"📚 API Docs: http://{host}:{port}/api/docs")
    logger.info(f"🔮 Oracle Interface: http://{host}:{port}/oracle")
    
    uvicorn.run(
        app, 
        host=host, 
        port=port,
        log_level="info",
        access_log=True
    )
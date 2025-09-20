# Oracle Creative Inspiration Tool - Cloud Deployment

## Cloud-Ready Oracle System

Complete AI-powered creative inspiration tool deployed to the cloud with the following components:

### Backend (`oracle_cloud.py`)
- FastAPI application optimized for production
- Gemini AI integration with fallback responses
- Multiple creativity levels (minimal, balanced, expansive)
- Health monitoring and API documentation
- CORS enabled for cross-origin access
- Production logging and error handling

### Frontend (`oracle_cloud_interface.html`)
- Cloud-aware interface that auto-detects environment
- Voice recognition and speech synthesis
- Real-time status indicator
- Responsive design for all devices
- Enhanced UI with creativity level selection

### Docker Container (`Dockerfile`)
- Python 3.11 slim base image
- Optimized for production deployment
- Health checks and security hardening
- Port 8001 exposed for web access

### Deployment Configuration
- `railway.toml` - Railway cloud deployment settings
- `requirements-docker.txt` - Production dependencies
- `.env` - Environment variables for API keys

## Deployment Instructions

### Railway Deployment
1. Push code to GitHub repository
2. Connect repository to Railway
3. Set GEMINI_API_KEY environment variable
4. Deploy automatically via Railway

### Manual Docker Deployment
```bash
# Build container
docker build -t oracle-cloud .

# Run container
docker run -p 8001:8001 -e GEMINI_API_KEY=your_api_key oracle-cloud
```

### Environment Variables
- `GEMINI_API_KEY` - Required for AI functionality
- `PORT` - Server port (default: 8001)  
- `HOST` - Server host (default: 0.0.0.0)

## API Endpoints

- `GET /` - Serve Oracle interface
- `GET /health` - Health check with status
- `POST /oracle/query` - Process creative queries
- `POST /oracle/speak` - Get speech-optimized responses
- `GET /oracle/inspire` - Random creative inspiration
- `GET /api/docs` - Interactive API documentation

## Features

- **AI-Powered Responses**: Gemini Pro integration with creative prompts
- **Voice Interface**: Speech recognition and text-to-speech
- **Cloud Native**: Auto-detects local vs production environment
- **Scalable Architecture**: Docker containerized for easy deployment
- **Monitoring Ready**: Health checks and structured logging
- **Creative Flexibility**: Multiple creativity levels and contexts

The Oracle Creative Inspiration Tool is now ready for public cloud deployment.
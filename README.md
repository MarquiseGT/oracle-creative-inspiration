# Oracle Creative Inspiration Tool 🔮

An AI-powered creative inspiration system that provides personalized guidance, actionable insights, and voice-enabled interaction for creative professionals, artists, writers, and innovators.

## ✨ Features

- **AI-Powered Responses**: Gemini Pro integration with intelligent creative prompts
- **Voice Interface**: Speech recognition and text-to-speech capabilities
- **Multiple Creativity Levels**: Minimal, balanced, and expansive response modes
- **Cloud-Native Architecture**: Docker containerized for scalable deployment
- **Real-Time Health Monitoring**: Built-in health checks and status indicators
- **Cross-Platform Compatibility**: Responsive web interface works on all devices

## 🚀 Live Demo

Visit the live Oracle: `https://your-app-name.railway.app` (URL provided after deployment)

## 🛠️ Technology Stack

- **Backend**: FastAPI with Python 3.11
- **AI Integration**: Google Gemini Pro API
- **Frontend**: Vanilla HTML/CSS/JavaScript with modern UI
- **Deployment**: Docker + Railway cloud platform
- **Voice Processing**: Web Speech API for recognition and synthesis

## 📱 Quick Start

### Option 1: Use the Live Version
Simply visit the deployed URL and start asking creative questions immediately.

### Option 2: Local Development
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/oracle-creative-inspiration.git
cd oracle-creative-inspiration

# Set up environment
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Install dependencies
pip install -r requirements-docker.txt

# Run locally
python oracle_cloud.py
```

## 🌐 API Endpoints

- `GET /` - Main Oracle interface
- `GET /health` - System health check
- `POST /oracle/query` - Process creative questions
- `POST /oracle/speak` - Get speech-optimized responses
- `GET /oracle/inspire` - Random creative inspiration
- `GET /api/docs` - Interactive API documentation

## 🎯 Use Cases

- **Creative Writing**: Get unstuck with character development, plot ideas, and narrative techniques
- **Design Challenges**: Explore new approaches to visual and UX design problems
- **Business Innovation**: Brainstorm solutions for product development and strategy
- **Personal Growth**: Receive guidance on creative blocks and skill development
- **Artistic Expression**: Discover new mediums and experimental approaches

## 🔧 Configuration

The Oracle automatically adapts to its environment:
- **Local Development**: Uses localhost endpoints
- **Cloud Deployment**: Auto-detects production URLs
- **API Integration**: Graceful fallback when AI services are unavailable

## 📊 Response Types

1. **AI-Generated** (`ai_generated`): Dynamic responses from Gemini Pro
2. **Curated Wisdom** (`curated_wisdom`): Handcrafted inspirational guidance
3. **Spontaneous** (`spontaneous`): Random creative prompts and challenges

## 🎨 Creativity Levels

- **Focused**: Concise, actionable creative direction
- **Balanced**: Thoughtful guidance with practical steps
- **Expansive**: Visionary exploration of creative possibilities

## 🔒 Privacy & Security

- No user data storage or tracking
- Secure HTTPS communication in production
- API keys managed through environment variables
- Container security with non-root user execution

## 🚀 Deployment

This application is designed for one-click deployment on Railway:

1. Fork this repository
2. Connect to Railway
3. Set `GEMINI_API_KEY` environment variable
4. Deploy automatically

## 📄 License

MIT License - Feel free to use, modify, and distribute.

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

*"Creative potential flows like water - it finds new paths when met with obstacles."* - The Oracle
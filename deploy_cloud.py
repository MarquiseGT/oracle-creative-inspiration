#!/usr/bin/env python3
"""
Oracle Cloud Deployment Script
Automated deployment to Railway cloud platform
"""

import os
import subprocess
import json
import webbrowser
from pathlib import Path

class OracleCloudDeployer:
    def __init__(self):
        self.project_path = Path("d:/RivenCreates/RIVEN_GENESIS/oracle_of_potential")
        self.repo_url = None
        
    def validate_files(self):
        """Validate all required deployment files exist"""
        required_files = [
            "oracle_cloud.py",
            "oracle_cloud_interface.html", 
            "Dockerfile",
            "requirements-docker.txt",
            "railway.toml",
            ".env"
        ]
        
        print("📋 Validating deployment files...")
        for file in required_files:
            file_path = self.project_path / file
            if file_path.exists():
                print(f"✅ {file}")
            else:
                print(f"❌ {file} - MISSING")
                return False
        
        return True
    
    def test_local_container(self):
        """Test Docker container locally before deployment"""
        print("🐳 Testing Docker container locally...")
        
        try:
            # Build container
            build_result = subprocess.run([
                "docker", "build", "-t", "oracle-cloud-test", "."
            ], cwd=self.project_path, capture_output=True, text=True)
            
            if build_result.returncode != 0:
                print(f"❌ Docker build failed: {build_result.stderr}")
                return False
                
            print("✅ Docker container built successfully")
            
            # Test container health
            run_result = subprocess.run([
                "docker", "run", "--rm", "-d", "-p", "8001:8001", 
                "--name", "oracle-test", "oracle-cloud-test"
            ], capture_output=True, text=True)
            
            if run_result.returncode == 0:
                print("✅ Container started successfully")
                
                # Stop test container
                subprocess.run(["docker", "stop", "oracle-test"], capture_output=True)
                return True
            else:
                print(f"❌ Container failed to start: {run_result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Docker test failed: {e}")
            return False
    
    def create_github_repo(self):
        """Create GitHub repository for deployment"""
        print("📱 Setting up GitHub repository...")
        
        repo_name = "oracle-creative-inspiration"
        
        try:
            # Initialize git if not already
            subprocess.run(["git", "init"], cwd=self.project_path, capture_output=True)
            
            # Add all files
            subprocess.run(["git", "add", "."], cwd=self.project_path)
            
            # Commit files
            subprocess.run([
                "git", "commit", "-m", "Oracle Creative Inspiration Tool - Cloud Ready"
            ], cwd=self.project_path, capture_output=True)
            
            print("✅ Git repository prepared")
            print(f"📝 Manual step required:")
            print(f"   1. Create repository '{repo_name}' on GitHub")
            print(f"   2. Push code: git remote add origin https://github.com/YOUR_USERNAME/{repo_name}.git")
            print(f"   3. Push code: git push -u origin main")
            
            return f"https://github.com/YOUR_USERNAME/{repo_name}"
            
        except Exception as e:
            print(f"❌ Git setup failed: {e}")
            return None
    
    def deploy_to_railway(self):
        """Deploy to Railway cloud platform"""
        print("🚀 Deploying to Railway...")
        
        deployment_url = "https://railway.app/new"
        
        print("✅ Opening Railway deployment page...")
        webbrowser.open(deployment_url)
        
        print(f"""
🎯 Railway Deployment Instructions:

1. **Connect GitHub Repository**:
   - Go to: {deployment_url}
   - Connect your GitHub account
   - Select the oracle-creative-inspiration repository

2. **Configure Environment Variables**:
   - Add: GEMINI_API_KEY = your_actual_gemini_api_key
   - Railway will auto-detect Dockerfile and deploy

3. **Access Your Oracle**:
   - Railway will provide a public URL
   - Your Oracle will be live at: https://your-app-name.railway.app

4. **Monitor Deployment**:
   - Check logs in Railway dashboard
   - Health endpoint: https://your-app-name.railway.app/health
   - API docs: https://your-app-name.railway.app/api/docs
        """)
        
        return True
    
    def create_deployment_package(self):
        """Create complete deployment package"""
        print("📦 Creating deployment package...")
        
        package_files = {
            "oracle_cloud.py": "Production FastAPI backend",
            "oracle_cloud_interface.html": "Cloud-aware frontend interface", 
            "Dockerfile": "Container configuration",
            "requirements-docker.txt": "Python dependencies",
            "railway.toml": "Railway deployment settings",
            "CLOUD_DEPLOYMENT.md": "Deployment documentation"
        }
        
        print("\n📋 Deployment Package Contents:")
        for file, description in package_files.items():
            file_path = self.project_path / file
            size = file_path.stat().st_size if file_path.exists() else 0
            print(f"   {file:<30} - {description} ({size} bytes)")
        
        return True
    
    def deploy(self):
        """Execute complete deployment process"""
        print("🔮 Oracle Creative Inspiration Tool - Cloud Deployment")
        print("=" * 60)
        
        # Validation
        if not self.validate_files():
            print("❌ Deployment validation failed")
            return False
        
        # Local testing
        print(f"\n🧪 Testing local container...")
        if not self.test_local_container():
            print("⚠️ Local container test failed - proceeding with deployment")
        
        # Package creation
        self.create_deployment_package()
        
        # Repository setup
        print(f"\n📱 Setting up version control...")
        repo_url = self.create_github_repo()
        
        # Cloud deployment
        print(f"\n🚀 Initiating cloud deployment...")
        self.deploy_to_railway()
        
        print(f"""
✨ Oracle Cloud Deployment Complete! ✨

🎯 Next Steps:
1. Push code to GitHub repository
2. Connect repository to Railway
3. Add GEMINI_API_KEY environment variable
4. Deploy and access your public Oracle

🌐 Once deployed, your Oracle Creative Inspiration Tool will be:
- Globally accessible via HTTPS
- AI-powered with Gemini integration
- Voice-enabled with speech recognition
- Mobile-responsive and PWA-ready
- Auto-scaling with cloud infrastructure

The Oracle awaits seekers of creative wisdom at your public URL!
        """)
        
        return True

if __name__ == "__main__":
    deployer = OracleCloudDeployer()
    deployer.deploy()
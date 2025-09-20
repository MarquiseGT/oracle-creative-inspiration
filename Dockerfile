# Use Python 3.11 slim image for optimal size and compatibility
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements-docker.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY oracle_cloud.py oracle_enhanced.py
COPY oracle_cloud_interface.html oracle_voice_interface.html
COPY .env .

# Create non-root user for security
RUN useradd -m -u 1000 oracle && chown -R oracle:oracle /app
USER oracle

# Expose port
EXPOSE 8001

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8001/health || exit 1

# Start the application
CMD ["python", "oracle_cloud.py"]
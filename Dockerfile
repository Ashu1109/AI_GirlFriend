# Backend Dockerfile
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# System deps (psycopg, build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first for better layer caching
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source
COPY . /app

# Expose the API port (Playground UI expects 7777)
EXPOSE 7777

# Default envs (can be overridden by docker-compose)
ENV PGVECTOR_URL=postgresql+psycopg://ai:ai@db:5432/ai

# Run the ASGI app via uvicorn directly to pin host/port
CMD ["python", "-m", "uvicorn", "girlfriend_agent:app", "--host", "0.0.0.0", "--port", "7777"]

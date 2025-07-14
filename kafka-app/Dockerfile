# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install build tools for dependencies (optional, only if needed)
RUN apt-get update && apt-get install -y gcc build-essential && rm -rf /var/lib/apt/lists/*

# Copy dependency definition files first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose FastAPI HTTP port (serves /metrics)
EXPOSE 9000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9003"]

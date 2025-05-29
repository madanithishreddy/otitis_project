FROM python:3.10.9-slim-buster

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies using uv
RUN uv pip install --system --no-cache -r requirements.txt

# Copy project
COPY . .

# Expose port 8000
EXPOSE 8000
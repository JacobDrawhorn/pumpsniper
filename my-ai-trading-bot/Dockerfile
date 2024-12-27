# A simple Dockerfile for containerizing your AI trading bot

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/
COPY training_data/ training_data/
COPY models/ models/
COPY README.md .
COPY main.py .  # (Optional if you really need a direct file)

# Expose default port (if any), e.g., 8080
# EXPOSE 8080

# Run the bot
CMD ["python", "src/main.py"] 
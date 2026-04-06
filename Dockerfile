FROM python:3.10

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose ports for API (7860) and Gradio (7861)
EXPOSE 7860
EXPOSE 7861

# Start script to run both processes
CMD ["sh", "-c", "python api/server.py & python app.py"]

FROM python:3.12

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install fastapi uvicorn

# Copy your FastAPI app into the container
COPY main.py .

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


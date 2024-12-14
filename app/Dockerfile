# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy required files
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code
COPY ./app ./app
COPY ./model ./model

# Expose the port FastAPI is running on
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
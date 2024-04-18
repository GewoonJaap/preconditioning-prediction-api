# Use the official Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY src/requirements.txt .

RUN apt-get update && apt-get install -y cmake ninja-build

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY src/ .

# Expose the port on which the Flask server will run
EXPOSE 8080

# Set the entrypoint command to start the Flask server
CMD ["python", "main.py"]
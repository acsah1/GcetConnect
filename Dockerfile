
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Expose the port Flask will run on
EXPOSE 5001    

# Run Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Use an official Python runtime as a parent image
# FROM python:3.10-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install dependencies
# RUN  pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # Set environment variables for Flask
# ENV FLASK_APP=run.py
# ENV FLASK_ENV=development

# # Expose the port Flask will run on
# EXPOSE 5001

# # Run Flask application
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]


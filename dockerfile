# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py .

# Install dependencies
RUN pip install flask

# Create a non-root user and switch to it
RUN useradd -m appuser
USER appuser

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

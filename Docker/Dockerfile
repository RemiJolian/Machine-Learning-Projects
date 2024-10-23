# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY iris_prediction.py .

# Install any dependencies
RUN pip install pandas scikit-learn matplotlib

# Command to run the application
CMD ["python", "iris_prediction.py"]

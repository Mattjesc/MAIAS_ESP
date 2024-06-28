# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME MAIAS_EmbeddedSystemsPrototyping

# Run the application
CMD ["python", "./src/MAIAS_EmbeddedSystemsPrototyping/main.py"]

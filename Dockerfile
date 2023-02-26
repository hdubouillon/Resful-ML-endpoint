# Use an official Python runtime as a parent image
FROM python:3.11.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME resful-ml-endpoint

# Run app.py when the container launches
CMD ["python", "app/app.py"]

# Run app.py and test it when the container launches
# CMD ["python", "-m", "unittest", "-s", "tests", "discover", "-p", "*_test.py"]
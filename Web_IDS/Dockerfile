# Use an official Python runtime as a parent image
FROM python:3.11.8

# Set the working directory in the container
WORKDIR /usr/src/app
#WORKDIR /mnt/c/ilja_wp/sideProject/dockerIDS-anti_bruteforce/myFlaskApp_IDS/myFlaskApp_IDS_docker

# Copy the current directory contents into the container at /usr/src/app
#COPY . .
COPY /mnt/c/ilja_wp/sideProject/dockerIDS-anti_bruteforce/myFlaskApp_IDS .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8083

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]


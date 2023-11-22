# Use Ubuntu as the base image
FROM ubuntu:20.04

# Update package lists and install wget and curl
RUN apt-get update && apt-get install -y wget curl

# Install Python and pip
RUN apt-get install -y python3 python3-pip

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

#RUN mkdir /data
# Set an entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Creat user to disable root login
RUN adduser --uid 1000 --home /app appuser && chown -R appuser /app
USER appuser
ENTRYPOINT ["/entrypoint.sh"]

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

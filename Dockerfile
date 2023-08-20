FROM python:3.10.12-slim-buster

# Update and install necessary Debian packages
RUN apt update -y && apt install -y \
    build-essential \
    software-properties-common \
    python3-pip

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy requirements.txt and the rest of the application to the container
COPY . /app

# Install Python requirements
RUN pip install -r requirements.txt

# These commands are based on your initial Dockerfile,
# I'm assuming you want to reinstall these packages after installing from requirements.txt.
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Command to run on container start
CMD ["python3", "app.py"]
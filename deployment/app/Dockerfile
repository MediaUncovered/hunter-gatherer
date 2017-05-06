# Set the base image to Ubuntu
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER todorus

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y git python python-dev python-distribute python-pip libpq-dev

# Install Python requirements
COPY deployment/api/requirements.txt /deployment/requirements.txt
RUN pip install -r /deployment/requirements.txt

# Copy app code
COPY    app   /app

# Start crawler
WORKDIR /app
CMD python hunter_gatherer.py

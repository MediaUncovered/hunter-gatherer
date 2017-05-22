# Set the base image to Ubuntu
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER todorus

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y git python3 python3-pip curl
# Install headless Selenium drivers
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs libfontconfig
RUN npm install -g phantomjs
ENV PATH="/usr/bin/phantomjs:${PATH}"
# Install newspaper ubuntu requirements
RUN apt-get install -y libxml2-dev libxslt-dev

# Install Python requirements
COPY deployment/app/requirements.txt /deployment/requirements.txt
RUN pip3 install -r /deployment/requirements.txt

# Copy app code
COPY    app   /app

# Start crawler
WORKDIR /app
CMD python hunter_gatherer.py

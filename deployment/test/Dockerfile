# Set the base image to Ubuntu
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER todorus

# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y git python python-dev python-distribute python-pip libpq-dev curl
# Install headless Selenium drivers
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs libfontconfig
RUN npm install -g phantomjs
ENV PATH="/usr/bin/phantomjs:${PATH}"

# Install Python requirements
COPY deployment/app/requirements.txt /deployment/app/requirements.txt
RUN pip install -r /deployment/app/requirements.txt
COPY deployment/test/requirements.txt /deployment/test/requirements.txt
RUN pip install -r /deployment/test/requirements.txt

# Install tests
COPY app /frame/app
COPY tests /frame/tests
COPY deployment/test/nose2.cfg /frame/nose2.cfg

# Start tests
WORKDIR /frame
CMD nose2 -c nose2.cfg --junit-xml

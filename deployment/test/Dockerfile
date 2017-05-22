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

# Install Python requirements
COPY deployment/app/requirements.txt /deployment/requirements.txt
RUN pip3 install -r /deployment/requirements.txt
COPY deployment/test/requirements.txt /deployment/test/requirements.txt
RUN pip3 install -r /deployment/test/requirements.txt

# Install newspaper ubuntu requirements
RUN apt-get install -y libxml2-dev libxslt-dev
RUN curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3

# Install tests
COPY app /frame/app
COPY tests /frame/tests
COPY deployment/test/nose2.cfg /frame/nose2.cfg
COPY deployment/test/coverage.cfg /frame/coverage.cfg

# Start tests
WORKDIR /frame
CMD nose2 -c nose2.cfg --junit-xml

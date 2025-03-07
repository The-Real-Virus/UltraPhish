# Dockerfile

# Author       : The-Real-Virus
# Github       : https://github.com/The-Real-Virus
# Email        : societycyber9@gmail.com
# Date         : 05-01-2025
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/The-Real-Virus/UltraPhish"

# Working directory
WORKDIR UltraPhish/
# Add files 
ADD . /UltraPhish

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install -r files/requirements.txt
RUN apt-get clean

# Main command
CMD ["python3", "UltraPhish.py", "--noupdate"]

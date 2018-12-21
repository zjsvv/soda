FROM python:3.7.1

ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /usr/src/app

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#sort-multi-line-arguments
RUN apt-get update && apt-get install -y \
    gettext \
    vim

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Copy source code to working directory
COPY . .

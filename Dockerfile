FROM python:3.8.13-slim-bullseye

# Do not write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Do not let Docker buffer console output
ENV PYTHONUNBUFFERED 1

WORKDIR /django_project

# Install dependencies
COPY ./requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

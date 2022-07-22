# syntax=docker/dockerfile:1

FROM python:3.7-alpine AS builder
# Run commands from /app directory inside container
WORKDIR /app/
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
# Copy requirements from local to docker image
COPY requirements.txt /app/
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt

FROM alpine
WORKDIR /app
# Copy everything from the current dir to the image
COPY --from=builder /app/ /app
EXPOSE 5000
CMD ["flask", "run"]

#!/bin/bash
IMAGE_NAME=bot_adapter

echo "Stopping and removing existing containers..."
docker-compose down

echo "Removing old Docker image..."
docker rmi $IMAGE_NAME

echo "Building and starting new containers..."
docker-compose up --build -d

echo "Process completed successfully."
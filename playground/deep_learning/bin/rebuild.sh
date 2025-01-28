#!/bin/bash

# Bring down the Docker containers
docker compose -f docker-compose.yml down

# Rebuild the Docker images without using the cache
docker compose -f docker-compose.yml build --no-cache

# Bring up the Docker containers
docker compose -f docker-compose.yml up -d --remove-orphans

#!/bin/bash

# Bring up the Docker containers
docker compose -f docker-compose.yml up -d --remove-orphans

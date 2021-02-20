#!/bin/bash
docker buildx build -t mershab99/IMAGE_NAME --platform --linux/arm/v7,linux/amd64 --push .

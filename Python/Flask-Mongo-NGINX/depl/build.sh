#!/bin/bash

docker build --tag=cannamaps .
docker tag cannamaps mershab99/cannamaps
docker push mershab99/cannamaps

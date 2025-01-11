#!/bin/bash

# Ensure the build is up-to-date
cd build
make

# Deploy the framework (this could involve copying binaries, setting up services, etc.)
# Example: Copy binaries to /usr/local/bin
sudo cp main /usr/local/bin/automated-pen-test-framework

echo "Deployment complete."
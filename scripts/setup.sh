#!/bin/bash

# Update package lists
sudo apt-get update

# Install necessary packages
sudo apt-get install -y build-essential cmake libpcap-dev python3 python3-pip

# Install Python dependencies
pip3 install -r requirements.txt

# Build C++ components
mkdir -p build
cd build
cmake ..
make

echo "Setup complete."
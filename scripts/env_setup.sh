#!/bin/bash

# Check if the script is run as root, if not, prompt to use sudo
if [[ $EUID -ne 0 ]]; then
   echo "Please run this script as root or with sudo" 
   exit 1
fi

# Update the system
echo "Updating system..."
apt-get update -y && apt-get upgrade -y

# Install essential tools
echo "Installing essential tools..."
apt-get install -y python3 python3-pip git curl docker.io

# Install Python packages
echo "Installing Python packages..."
pip3 install --upgrade pip
pip3 install flask boto3 requests

# Verify installations
echo "Verifying installations..."
python3 --version
git --version
docker --version

echo "Environment setup complete!"

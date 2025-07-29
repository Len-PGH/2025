#!/bin/bash

# This script sets up the environment and installs dependencies for the LED Control Agent project.

echo "Starting setup..."

# Update pip to the latest version
pip install --upgrade pip

# Install required Python packages
pip install signalwire-agents requests

echo "Dependencies installed successfully."

# Optional: Create a virtual environment if needed
# python -m venv venv
# source venv/bin/activate
# pip install signalwire-agents requests

echo "Setup complete. You can now run the agent with 'python agent.py'."

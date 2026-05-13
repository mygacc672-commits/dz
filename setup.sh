#!/bin/bash
echo "🔧 Setting up Termux Hacking Tools..."

# Update package manager
pkg update -y && pkg upgrade -y

# Install dependencies for Termux (ping, whois, nmap)
pkg install ping whois nmap python -y

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup complete! Run tools/scanner.py to start."

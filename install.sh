#!/data/data/com.termux/files/usr/bin/bash
# SocialSnap Installer for Termux
# Created by Tanaka Mucheke

echo "================================"
echo "  ArtNamer- Termux Installer by Tanaka Mucheke"
echo "================================"

# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install -y python git 

# Install Python modules
pip install colorama 

# Clone the repo if not already present (optional)
if [ ! -f "Art_name.py" ]; then
    git clone https://github.com/Tanakaprogramminghub/ArtNamer.git .
fi

echo "Installation complete. Run 'python Art_name.py' to start."
#!/bin/bash

echo ""
echo "  ██╗  ██╗███████╗████████╗██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗"
echo "  ███╗ ██║██╔════╝╚══██╔══╝██║  ██║██╔══██╗██║    ██║██║ ██╔╝"
echo "  ████╗██║█████╗     ██║   ███████║███████║██║ █╗ ██║█████╔╝ "
echo "  ██╔████║██╔══╝     ██║   ██╔══██║██╔══██║██║███╗██║██╔═██╗ "
echo "  ██║╚███║███████╗   ██║   ██║  ██║██║  ██║╚███╔███╔╝██║  ██╗"
echo "  ╚═╝ ╚══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝"
echo ""
echo "  [*] NetHawk Setup Script"
echo "  [*] by MelodicSam"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "  [!] Please run as root: sudo bash setup.sh"
  exit 1
fi

echo "  [*] Updating package list..."
apt-get update -qq

echo "  [*] Installing Python dependencies..."
pip install rich requests --break-system-packages -q

echo "  [*] Installing system tools..."
apt-get install -y -qq net-tools iproute2 iputils-ping 2>/dev/null

echo "  [*] Setting execute permissions..."
chmod +x nethawk.py

echo "  [*] Creating nethawk command..."
cp nethawk.py /usr/local/bin/nethawk
chmod +x /usr/local/bin/nethawk
sed -i '1s|.*|#!/usr/bin/env python3|' /usr/local/bin/nethawk

echo ""
echo "  [✓] Setup complete!"
echo "  [✓] Run with: python3 nethawk.py"
echo "  [✓] Or simply: nethawk"
echo ""

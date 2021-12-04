#!/bin/bash
cat $(pwd)/aalu.py > /bin/aalu
chmod +x /bin/aalu
echo "[+] Installed Successfully!"
echo "[+] type `aalu --help` in the shell"

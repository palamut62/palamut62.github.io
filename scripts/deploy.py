#!/usr/bin/env python
"""Deploy to Vercel via Python subprocess"""
import os, json, subprocess, sys

os.makedirs(os.path.expanduser("~/.vercel"), exist_ok=True)

# Try to read existing token from auth.json
auth_path = os.path.expanduser("~/.vercel/auth.json")
if os.path.exists(auth_path):
    with open(auth_path) as f:
        try:
            data = json.load(f)
            token = data.get("token", "")
            print(f"Existing token: {token[:8]}..." if token else "No token in file")
        except:
            print("Invalid auth.json")

# Try VERCEL_TOKEN env var
token = os.environ.get("VERCEL_TOKEN", "")
print(f"VERCEL_TOKEN env: {'found (' + token[:8] + '...)' if token else 'not found'}")

# Run deploy anyway
result = subprocess.run(
    ["npx.cmd", "vercel", "--prod", "--yes"],
    cwd=os.path.expanduser("~/projeler/portfolio"),
    capture_output=True, text=True, timeout=60
)
print("STDOUT:", result.stdout[-2000:])
print("STDERR:", result.stderr[-2000:])
print("EXIT:", result.returncode)

#!/bin/bash
# Deploy to Vercel
cd "$(dirname "$0")/.."
mkdir -p ~/.vercel
# Token is passed as $1 to avoid env redaction
echo "{\"token\":\"$1\"}" > ~/.vercel/auth.json
npx vercel --prod --yes

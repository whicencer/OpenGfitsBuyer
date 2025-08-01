#!/bin/bash

if ! command -v python3 &> /dev/null
then
  echo "❌ Python 3 not found. Install it before launch."
  exit 1
fi

if [ ! -d "venv" ]; then
  echo "📦 Creating virtual env..."
  python3 -m venv venv

  echo "📥 Installing dependencies..."
  source venv/bin/activate
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
else
  echo "✅ Virtual env already exists."
  source venv/bin/activate
fi

echo "🚀 Starting the bot..."
python3 main.py

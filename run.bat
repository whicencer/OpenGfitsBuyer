@echo off

where python >nul 2>nul
if errorlevel 1 (
  echo ❌ Python not found. Install it and add it to PATH.
  exit /b 1
)

python -m venv venv

call venv\Scripts\activate.bat

pip install --upgrade pip
pip install -r requirements.txt

python main.py
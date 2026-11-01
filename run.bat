@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe py -m venv .venv
call .venv\Scripts\activate
python -m pip install -r requirements.txt
if not exist .env (
  echo Copy .env.example to .env and add your API keys.
  pause
  exit /b 1
)
python server.py
pause

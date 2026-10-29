@echo off
setlocal
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (
  echo Python was not found.
  echo Install Python from https://www.python.org/downloads/windows/
  echo Check "Add python.exe to PATH", then reopen this file.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  python -m venv .venv
  if errorlevel 1 goto failed
)
echo Installing/checking Flask...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo Starting Mentor at http://127.0.0.1:8000
".venv\Scripts\python.exe" app.py
goto done
:failed
echo Setup failed. See README.md and the error above.
pause
:done
endlocal

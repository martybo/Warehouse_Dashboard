@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Move to the script's directory
cd /d %~dp0

:: Check for virtual environment
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo 🔧 Creating virtual environment...
    python -m venv venv
)

:: Activate venv and install requirements
call venv\Scripts\activate.bat
pip install --quiet pandas PyGithub python-dotenv

:: Run script and log output
echo 🟢 Running auto_convert_and_push_v1_0_4.py...
python auto_convert_and_push_v1_0_4.py > output.txt 2>&1

echo ✅ Done. See output.txt for details.
pause

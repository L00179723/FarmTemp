@echo off
echo Welcome to Project Farm!

REM Set the project directory
set "project_directory=C:\Users\suzan\Desktop"

REM Change to the project directory
cd /d %project_directory%

REM Display project information
echo Project Name: Farming System
echo Location: %project_directory%
echo.

REM Execute project-related commands
echo Running project_directoryFarm...
python farm_simulation.py

REM Add more commands as needed

REM Pause to keep the command prompt window open (optional)
pause

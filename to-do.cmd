@echo off
set work_directory=%~p0
pushd %work_directory%
call %work_directory%\.venv\scripts\activate
call py .\main.py
pause
exit
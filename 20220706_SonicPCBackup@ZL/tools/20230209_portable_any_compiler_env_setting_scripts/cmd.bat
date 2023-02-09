@echo off
call "%~dp0env_for_icons.bat"  %*
if not "%WORKDIR%"=="%WORKDIR1%" cd %WORKDIR1%
cmd.exe /k
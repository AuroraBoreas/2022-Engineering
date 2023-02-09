@echo off
set DIRBASE=%~dp0..

rem get a normalize path
set DIRBASETMP=%~dp0..
pushd %DIRBASETMP%
set DIRBASE=%__CD__%
if "%DIRBASE:~-1%"=="\" set DIRBASE=%DIRBASE:~0,-1%
set DIRBASETMP=
popd

set DIR=%DIRBASE%\openjdk-19.0.2\bin
set JAVA=%DIR%\java.exe
set JAVAVER=19.0.2
set ARCH=WIN32
set FINDDIR=%WINDIR%\system32
echo ";%PATH%;" | %FINDDIR%\find.exe /C /I ";%DIR%\;" >nul
if %ERRORLEVEL% NEQ 0 (
   set "PATH=%DIR%\;%PATH%;"
   cd .
)
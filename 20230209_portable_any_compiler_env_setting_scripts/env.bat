@echo off
set JAVADIRBASE=%~dp0..

rem get a normalize path
set JAVADIRBASETMP=%~dp0..
pushd %JAVADIRBASETMP%
set JAVADIRBASE=%__CD__%
if "%JAVADIRBASE:~-1%"=="\" set JAVADIRBASE=%JAVADIRBASE:~0,-1%
set JAVADIRBASETMP=
popd

set JAVADIR=%JAVADIRBASE%\openjdk-19.0.2\bin
set JAVA=%JAVADIR%\java.exe
set JAVAVER=19.0.2
set JAVAARCH=WIN32
set FINDDIR=%WINDIR%\system32
echo ";%PATH%;" | %FINDDIR%\find.exe /C /I ";%JAVADIR%\;" >nul
if %ERRORLEVEL% NEQ 0 (
   set "PATH=%JAVADIR%\;%PATH%;"
   cd .
)
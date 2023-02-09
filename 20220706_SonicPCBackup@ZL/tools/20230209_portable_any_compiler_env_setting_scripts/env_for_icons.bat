@echo off
call "%~dp0env.bat"

rem default is as before: Winpython ..\Notebooks
set WORKDIR1=%DIRBASE%

rem if we have a file or directory in %1 parameter, we use that directory 
if not "%~1"=="" (
   if exist "%~1" (
      if exist "%~1\" (
         rem echo it is a directory %~1
	     set WORKDIR1=%~1
	  ) else (
	  rem echo  it is a file %~1, so we take the directory %~dp1
	  set WORKDIR1=%~dp1
	  )
   )
) else (
rem if it is launched from another directory , we keep it that one echo %__CD__%
if not "%__CD__%"=="%~dp0" set  WORKDIR1="%__CD__%"
)
rem remove potential doublequote
set WORKDIR1=%WORKDIR1:"=%
rem remove some potential last \
if "%WORKDIR1:~-1%"=="\" set WORKDIR1=%WORKDIR1:~0,-1%
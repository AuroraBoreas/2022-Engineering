@echo off
call "%~dp0env.bat"

rem default is as before: Winpython ..\Notebooks
set JAVAWORKDIR1=%JAVADIRBASE%

rem if we have a file or directory in %1 parameter, we use that directory 
if not "%~1"=="" (
   if exist "%~1" (
      if exist "%~1\" (
         rem echo it is a directory %~1
	     set JAVAWORKDIR1=%~1
	  ) else (
	  rem echo  it is a file %~1, so we take the directory %~dp1
	  set JAVAWORKDIR1=%~dp1
	  )
   )
) else (
rem if it is launched from another directory , we keep it that one echo %__CD__%
if not "%__CD__%"=="%~dp0" set  JAVAWORKDIR1="%__CD__%"
)
rem remove potential doublequote
set JAVAWORKDIR1=%JAVAWORKDIR1:"=%
rem remove some potential last \
if "%JAVAWORKDIR1:~-1%"=="\" set JAVAWORKDIR1=%JAVAWORKDIR1:~0,-1%
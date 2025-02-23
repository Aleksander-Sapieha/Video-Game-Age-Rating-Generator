@echo off

echo Installing Pyinstaller...

pip install pyinstaller

echo Compiling...
pyinstaller src/main.py --onefile

@ECHO OFF
REM 

rmdir /S /Q build
python setup.py sdist
echo "final whl package will be in dist folder"
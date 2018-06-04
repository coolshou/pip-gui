@ECHO OFF
REM 

rmdir /S /Q build
del dist/*
python setup.py sdist
echo "final whl package will be in dist folder"
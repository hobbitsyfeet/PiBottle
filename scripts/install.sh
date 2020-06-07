#!/bin/sh
cd "$(dirname "$0")"

python -m venv ../env
../env/Scripts/activate.bat
python -m pip install -r ../requirments.txt
pyinstaller --onefile ../Pibottle.py
pause
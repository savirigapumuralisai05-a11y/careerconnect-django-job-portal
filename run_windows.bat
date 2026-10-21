@echo off
py -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations accounts jobs applications
python manage.py migrate
python manage.py runserver
pause

python3.11 -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata "documents\dummy_data.json"
python manage.py runserver


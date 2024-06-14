# python 3.10.12

to run the project

1. Create virtual environment
python -m venv virtuenv

2. Activate
source ./venv/bin/activate

3. install requirements
pip install -r requirements.txt

4. run migrations
python manage.py makemigrations
python manage.py migrate

5. run the project
python manage.py runserver

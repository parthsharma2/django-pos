# django-pos
A point of sale system implemented in django.

--------------------------------------------
## Setup
1. Clone this project.
```
git clone https://github.com/parthsharma2/django-pos.git
```

2. Move into the cloned project's directory.
```
cd django-pos
```

3. Create a python 3 virtual environment and activate it.
```
python3 -m venv env
```
```
source env/bin/activate
```

4. Install the requirements.
```
pip install -r requirements.txt
```

5. Make database migrations.
```
python manage.py makemigrations
```
```
python manage.py migrate
```

6. Run the application.
```
python manage.py runserver
```

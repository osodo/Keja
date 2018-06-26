# Keja

## Linux
## Requirements 
* Python 3.6
* virtualenv
* Django 2.0.1 and above
* Text editor :joy: :joy:
* Requirements file for additional python packages

## Installation
* virtualenv -p /usr/bin/python3.6 --no-site-packages { **folder name eg Keja** }
* cd { **folder name eg Keja** }
* source bin/activate
* git clone [GitHub Repository](https://github.com/osodo/Keja)
* cd Keja
* pip install -r Requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py collectstatic
> add a user, caretaker and house through the admin panel atleast 5
* python manage.py runserver 8080
